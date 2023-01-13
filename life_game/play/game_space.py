from dataclasses import dataclass
import random
from life_game.setup.players import Player
from life_game.play.actions import select_card, play_card


@dataclass
class Game:
    players: dict[int, Player]

    


    def play_round(
        self, round: str) -> None:

            deal = deal_cards()

            for x in turns:
                play_turn()

            resolve_events()

        for player in num_players:
            hand = game_space.player_info[player].hand
            board = game_space.player_info[player].board

            chosen_cards = select_card(hand)

            for card in chosen_cards:
                game_space.player_info[player].board = play_card(board, hand, card)

    
