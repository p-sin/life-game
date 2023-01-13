from life_game.setup.components import Board, attribute_slots, rounds
from life_game.setup.cards import cards, card_type
from life_game.setup.logic import Logic
from life_game.setup.deal import deal_type

from dataclasses import dataclass
from typing import Optional, Tuple

hand_type = dict[int, card_type]


@dataclass
class Player:
    board: Board
    child_hand: hand_type
    adol_hand: hand_type
    adult_hand: hand_type
    logic: Optional[Logic] = None


def select_player_cards(
    deals: dict[str, list[int]], player: int
) -> Tuple[dict[int, card_type], dict[int, card_type], dict[int, card_type]]:
    player_cards: dict[str, dict[int, card_type]] = {}

    for round in rounds:
        start = 0 + (9 * (player - 1))
        end = 9 + (9 * (player - 1))
        player_deal = deals[round][start:end]

        for num, card in enumerate(player_deal):
            player_cards[round] = {num + 1: cards[card]}

    return (player_cards["child"], player_cards["adol"], player_cards["adult"])


def create_players(total_players: int, deals: deal_type) -> dict[int, Player]:
    players = {}

    for iter, _ in enumerate(range(total_players)):
        board = Board(iter + 1, attribute_slots)
        child_hand, adol_hand, adult_hand = select_player_cards(deals, iter + 1)
        logic = Logic()
        players[iter + 1] = Player(board, child_hand, adol_hand, adult_hand, logic)

    return players
