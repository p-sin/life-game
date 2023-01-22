from life_game.setup.components import Board, attribute_slots, rounds
from life_game.setup.attr_cards import cards, card_type
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
    """Utility function for extracting required information from a card when playing it"""
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
    """The player object defines each player in the game and holds all their information (board, cards, points, etc.)
    The methods in the player object are used to drive much of the activity in the game
    """

    board: Board
    child_hand: hand_type
    adol_hand: hand_type
    adult_hand: hand_type
    logic: Optional[Logic] = None

    def choose_cards(self, round: str, turn: int) -> Tuple[list[card_type], list[int]]:
        """Apply the players logic module to select two cards to play"""
        # Currently picks two cards at random from within the range of cards in their hand (determined by the turn)
        possible_pos = [x for x in range(1, 10 - (2 * (turn - 1)))]
        chosen_cards_pos = random.sample(possible_pos, 2)
        round_hand = getattr(self, rounds[round])
        # Return list of the two card objects and a list of the two cards positions in the hand
        return [round_hand[card] for card in chosen_cards_pos], chosen_cards_pos

    def play_cards(self, chosen_cards: list[card_type]) -> None:
        """Extract each card's information and apply it to the correct attribute slot on the player's board"""
        for card in chosen_cards:
            for card_slot in ["card_slot_1", "card_slot_2", "card_slot_3"]:
                attr_slot, value_name, value_value = extract_card_info(card, card_slot)

                if value_name is not None:
                    self.board.attribute_slots[attr_slot]["type"] = value_name
                    self.board.attribute_slots[attr_slot]["value"] = value_value

    def remove_cards(self, chosen_cards_pos: list[int], round: str) -> None:
        """For each card in the player's hand, check if it is in the position of one of the two cards played.
        If it isn't, add it to a new hand object. Make the new hand object the players new hand
        """
        hand: hand_type = getattr(self, rounds[round])
        new_hand: hand_type = {}
        new_pos = 1
        for old_pos, (_, card) in enumerate(hand.items()):
            # If the position of the card is not one of the two cards played
            if (old_pos + 1) not in chosen_cards_pos:
                new_hand[new_pos] = card
                new_pos += 1

        setattr(self, rounds[round], new_hand)

    def calculate_attribute_totals(self) -> None:
        """Calculate the total value of each attribute and then set the player's board totals to those values"""
        attribute_totals = copy.deepcopy(attribute_total_calc)
        for _, stats in self.board.attribute_slots.items():
            if stats["type"] != "":
                attribute_totals[stats["type"]] += stats["value"]

        for attribute, total in attribute_totals.items():
            setattr(self.board, attribute, total)

    def apply_events(self, events) -> None:
        pass


def select_player_deal(deals: deal_type, player: int, round: str) -> list[int]:
    """Slice the deal (list of ints) for 9 cards, which 9 cards is determined by the player number"""
    start = 0 + (9 * (player - 1))
    end = 9 + (9 * (player - 1))
    return deals[round][start:end]


def select_player_cards(
    deals: deal_type, player: int
) -> Tuple[dict[int, card_type], dict[int, card_type], dict[int, card_type]]:
    """Each player gets a hand for each round. This is the 'next' 9 cards which are taken from the deal.
    The relevant card information is taken from the cards object and put into a dictionary of cards denoting
    their hand"""
    player_cards: dict[str, dict[int, card_type]] = {}

    for round in rounds.keys():
        player_deal = select_player_deal(deals, player, round)
        player_cards[round] = {}
        for num, card in enumerate(player_deal):
            player_cards[round].update({num + 1: cards[card]})

    return (player_cards["child"], player_cards["adol"], player_cards["adult"])


def create_players(total_players: int, deals: deal_type) -> dict[int, Player]:
    """Create a dictionary of players. Each player takes an empty board, 3 hands and
    some AI logic"""
    players = {}

    for iter, _ in enumerate(range(total_players)):
        board = Board(copy.deepcopy(attribute_slots))
        child_hand, adol_hand, adult_hand = select_player_cards(deals, iter + 1)
        logic = Logic()
        players[iter + 1] = Player(board, child_hand, adol_hand, adult_hand, logic)

    return players
