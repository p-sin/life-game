from dataclasses import dataclass
from life_game.play.players import Player


@dataclass
class Game:
    players: dict[int, Player]

    def card_phase(self, round: str):
        for _, player in self.players.items():
            chosen_cards = player.choose_cards(round)
            player.play_cards(chosen_cards)
