from dataclasses import dataclass
from life_game.play.players import Player, hand_type
from life_game.setup.components import rounds, turns


@dataclass
class Game:
    total_players: int
    players: dict[int, Player]

    def card_phase(self, round: str, turn: int):
        for _, player in self.players.items():
            chosen_cards, chosen_cards_pos = player.choose_cards(round, turn)
            player.play_cards(chosen_cards)
            player.remove_cards(chosen_cards_pos, round)
            player.calculate_attribute_totals()

    def pass_hand(self, round: str) -> None:
        dummy_hand: hand_type = getattr(self.players[self.total_players], rounds[round])

        for player in range(self.total_players, 1, -1):
            setattr(
                self.players[player],
                rounds[round],
                getattr(self.players[player - 1], rounds[round]),
            )

        setattr(self.players[1], rounds[round], dummy_hand)

    def event_phase(self) -> None:
        pass

    def play_turn(self, round: str, turn: int) -> None:
        self.card_phase(round, turn)
        self.pass_hand(round)
        self.event_phase()

    def play_round(self, round: str) -> None:
        for turn in turns:
            self.play_turn(round, turn)

    def play_game(self) -> None:
        for round in rounds:
            self.play_round(round)
