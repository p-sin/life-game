from life_game.setup.components import Board, decks, attribute_slots
from life_game.setup.cards import cards, card_type
from life_game.setup.logic import Logic
from life_game.setup.setup_exceptions import (
    InvalidPlayerCountRange,
    InvalidPlayerCountType,
)

from dataclasses import dataclass
from typing import Optional, Tuple
import random

hand_type = Optional[dict[int, card_type]]


@dataclass
class Player:
    board: Board
    hand: hand_type = None
    logic: Optional[Logic] = None


@dataclass
class GameSpace:
    player_info: dict[int, Player]


def setup_players(total_players: int) -> Tuple[GameSpace, list[int]]:
    def player_count(total_players) -> list[int]:
        return [x for x in range(1, total_players + 1)]

    def create_players(num_players: list[int]) -> GameSpace:
        player_info = {}

        for id in num_players:
            board = Board(id, attribute_slots)
            hand = None
            logic = Logic()
            player_info[id] = Player(board, hand, logic)

        return GameSpace(player_info)

    if not isinstance(total_players, int):
        raise InvalidPlayerCountType(total_players)
    elif not 0 < total_players < 7:
        raise InvalidPlayerCountRange(total_players)
    else:
        num_players = player_count(total_players)
        game_space = create_players(num_players)

    return game_space, num_players
