from life_game.setup.components import Board, attribute_slots, rounds
from life_game.setup.cards import cards, card_type
from life_game.setup.logic import Logic
from life_game.setup.deal import deal_type

from dataclasses import dataclass
from typing import Optional, Tuple
import random

hand_type = dict[int, card_type]


def map_round_to_hand(round: str) -> str:
    return round + "_hand"


@dataclass
class Player:
    board: Board
    child_hand: hand_type
    adol_hand: hand_type
    adult_hand: hand_type
    logic: Optional[Logic] = None

    def choose_cards(self, round: str) -> list[card_type]:
        chosen_card_nums = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
        round_hand = getattr(self, map_round_to_hand(round))

        return [round_hand[card] for card in chosen_card_nums]

    def play_cards(self, round: str, chosen_cards: list[card_type]):
        pass


def select_player_deal(deals: deal_type, player: int, round: str) -> list[int]:
    start = 0 + (9 * (player - 1))
    end = 9 + (9 * (player - 1))
    return deals[round][start:end]


def select_player_cards(
    deals: deal_type, player: int
) -> Tuple[dict[int, card_type], dict[int, card_type], dict[int, card_type]]:
    player_cards: dict[str, dict[int, card_type]] = {}

    for round in rounds:
        player_deal = select_player_deal(deals, player, round)
        player_cards[round] = {}
        for num, card in enumerate(player_deal):
            player_cards[round].update({num + 1: cards[card]})

    return (player_cards["child"], player_cards["adol"], player_cards["adult"])


def create_players(total_players: int, deals: deal_type) -> dict[int, Player]:
    players = {}

    for iter, _ in enumerate(range(total_players)):
        board = Board(attribute_slots)
        child_hand, adol_hand, adult_hand = select_player_cards(deals, iter + 1)
        logic = Logic()
        players[iter + 1] = Player(board, child_hand, adol_hand, adult_hand, logic)

    return players
