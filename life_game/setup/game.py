from setup.components import Board, decks, attribute_slots
from setup.cards import cards, card_type
from setup.logic import Logic

from dataclasses import dataclass
from typing import Optional, Tuple
import random

hand_type = dict[int, Optional[card_type]]

@dataclass
class Player:
    board: Board
    hand: Optional[hand_type] = None
    logic: Optional[Logic] = None


@dataclass
class GameSpace:
    player_info: dict[int, Player]


 
def setup_players() -> Tuple[dict[int, Player], list[int]]:

    def player_count () -> list[int]:
        return [1,2]

    def create_players(num_players: list[int]) -> dict[int, Player]:

        player_info = {}

        for id in num_players:
            board = Board(id, attribute_slots)
            hand = None
            logic = Logic()
            player_info[id] = Player(board, hand, logic)
            
        return player_info

    num_players = player_count()
    player_info = create_players(num_players)
  
    return player_info, num_players


def deal_cards(game_space: GameSpace, round: str, num_players: list[int]) -> GameSpace:

    def select_player_cards (deal: list[int], player: int) -> dict[int, card_type]:

        start = 0 + (9 * (player - 1))
        end = 9 + (9 * (player - 1))
        player_deal = deal[start: end]

        player_cards = {}

        for num, card in enumerate(player_deal):
            player_cards[num + 1] = cards[card]

        return player_cards

    deal = random.sample(decks[round], len(num_players) * 9)

    for player in num_players:
        
        player_cards = select_player_cards(deal, player)

        game_space.player_info[player].hand = player_cards

    return game_space

  