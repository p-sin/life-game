from life_game.setup.components import Board, attribute_slots, rounds
from life_game.setup.cards import cards, card_type
from life_game.setup.logic import Logic
from life_game.setup.deal import deal_type
from life_game.play.play_utils import attribute_total_calc

from dataclasses import dataclass
from typing import Optional, Tuple, Union
import random
import copy

hand_type = dict[int, card_type]


def extract_card_info(
    card: card_type, card_slot: str
) -> Tuple[Union[str, None], Union[str, None], Union[int, None]]:
    if card[card_slot]["slot_number"] is not None:
        return (
            card[card_slot]["slot_number"],
            card[card_slot]["values"].value.name,
            card[card_slot]["values"].value.value,
        )
    else:
        return None, None, None


@dataclass
class Player:
    board: Board
    child_hand: hand_type
    adol_hand: hand_type
    adult_hand: hand_type
    logic: Optional[Logic] = None

    def choose_cards(self, round: str) -> list[card_type]:
        # HANDLE EACH TURN WITH FEWER CARDS
        chosen_card_pos = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
        round_hand = getattr(self, rounds[round])

        return [round_hand[card] for card in chosen_card_pos]

    def play_cards(self, chosen_cards: list[card_type]) -> None:
        for card in chosen_cards:
            for card_slot in ["card_slot_1", "card_slot_2", "card_slot_3"]:
                attr_slot, value_name, value_value = extract_card_info(card, card_slot)

                if value_name is not None:
                    self.board.attribute_slots[attr_slot]["type"] = value_name
                    self.board.attribute_slots[attr_slot]["value"] = value_value

    def remove_cards(self, chosen_cards: list[card_type], round: str) -> None:
        chosen_cards_nums = [chosen_cards[0]["number"], chosen_cards[1]["number"]]

        hand: hand_type = getattr(self, rounds[round])
        new_hand: hand_type = {}
        pos = 1
        for _, card in hand.items():
            if card["number"] not in chosen_cards_nums:
                new_hand[pos] = card
                pos += 1

        setattr(self, rounds[round], new_hand)

    def calculate_attribute_totals(self) -> None:
        attribute_totals = copy.deepcopy(attribute_total_calc)
        for _, stats in self.board.attribute_slots.items():
            if stats["type"] != "":
                attribute_totals[stats["type"]] += stats["value"]

        for attribute, total in attribute_totals.items():
            setattr(self.board, attribute, total)


def select_player_deal(deals: deal_type, player: int, round: str) -> list[int]:
    start = 0 + (9 * (player - 1))
    end = 9 + (9 * (player - 1))
    return deals[round][start:end]


def select_player_cards(
    deals: deal_type, player: int
) -> Tuple[dict[int, card_type], dict[int, card_type], dict[int, card_type]]:
    player_cards: dict[str, dict[int, card_type]] = {}

    for round in rounds.keys():
        player_deal = select_player_deal(deals, player, round)
        player_cards[round] = {}
        for num, card in enumerate(player_deal):
            player_cards[round].update({num + 1: cards[card]})

    return (player_cards["child"], player_cards["adol"], player_cards["adult"])


def create_players(total_players: int, deals: deal_type) -> dict[int, Player]:
    players = {}

    for iter, _ in enumerate(range(total_players)):
        board = Board(copy.deepcopy(attribute_slots))
        child_hand, adol_hand, adult_hand = select_player_cards(deals, iter + 1)
        logic = Logic()
        players[iter + 1] = Player(board, child_hand, adol_hand, adult_hand, logic)

    return players
