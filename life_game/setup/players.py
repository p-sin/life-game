from life_game.setup.components import Board, attribute_slots
from life_game.setup.cards import card_type
from life_game.setup.logic import Logic
from life_game.setup.deal import select_player_cards, deal_type


from dataclasses import dataclass
from typing import Optional

hand_type = dict[int, card_type]


@dataclass
class Player:
    board: Board
    child_hand: hand_type
    adol_hand: hand_type
    adult_hand: hand_type
    logic: Optional[Logic] = None


def create_players(total_players: int, deals: deal_type) -> dict[int, Player]:
    num_players = [x for x in range(1, total_players + 1)]
    players = {}

    for id in num_players:
        board = Board(id, attribute_slots)
        child_hand, adol_hand, adult_hand = select_player_cards(deals, id)
        logic = Logic()
        players[id] = Player(board, child_hand, adol_hand, adult_hand, logic)

    return players
