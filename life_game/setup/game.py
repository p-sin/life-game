from setup.components import Board, decks, attribute_slots
from setup.comps_2 import base_hand, hand_type
from setup.cards import cards, card_type
from setup.logic import Logic


from dataclasses import dataclass
from typing import Optional, Tuple
import random


@dataclass
class Player:
    board: Board
    hand: hand_type
    logic: Optional[Logic] = None


@dataclass
class GameSpace:
    player_info: dict[int, Player]


 
def setup_players() -> Tuple[dict[int, Player], list[int]]:

    def define_players () -> list[int]:
        return [1,2,3,4]

    def create_players(num_players: list[int]) -> dict[int, Player]:

        player_info = {}

        for id in num_players:
            board = Board(id, attribute_slots)
            hand = base_hand
            logic = Logic()
            player_info[id] = Player(board, hand, logic)

        return player_info

    num_players = define_players()
    player_info = create_players(num_players)
    
    return player_info, num_players


def deal_cards(game_space: GameSpace, round: str, num_players: list[int]) -> GameSpace:

    deal = random.sample(decks[round], len(num_players) * 9)

    for player in num_players:
        for num in range (1, 10):
            game_space.player_info[player].hand[str(num)] = cards[num + (9 * (player - 1))]

    return game_space
        


