from dataclasses import dataclass
from life_game.play.players import Player, hand_type
from life_game.setup.components import rounds, turns
from life_game.setup.event_cards import event_type

{
    "child": {
        1: {},
        2: {},
    }
}


@dataclass
class Game:
    """Main control object. Contains all the components of the game and manages the control flow"""

    total_players: int
    players: dict[int, Player]
    events: dict[str, dict[int, event_type]]

    def card_phase(self, round: str, turn: int):
        """ "The phase of each player choosing and playing cards and updating their board"""
        for _, player in self.players.items():
            chosen_cards, chosen_cards_pos = player.choose_cards(round, turn)
            player.play_cards(chosen_cards)
            player.remove_cards(chosen_cards_pos, round)
            player.calculate_attribute_totals()

    def pass_hand(self, round: str) -> None:
        """Passing each players hand on to the next player"""
        # Whoever the last player is, passes their card to a dummy player
        dummy_hand: hand_type = getattr(self.players[self.total_players], rounds[round])

        # Each player gets the hand of the player before them, except player 1
        for player in range(self.total_players, 1, -1):
            setattr(
                self.players[player],
                rounds[round],
                getattr(self.players[player - 1], rounds[round]),
            )

        # Player 1 then gets their hand from the dummy player (originally the hand of the last player)
        setattr(self.players[1], rounds[round], dummy_hand)

    def select_events(self, round: str) -> None:
        pass

    def event_phase(self, round: str) -> None:
        events = self.select_events(round)
        for _, player in self.players.items():
            player.apply_events(events)

    def play_turn(self, round: str, turn: int) -> None:
        """Control flow for a turn"""
        self.card_phase(round, turn)
        self.pass_hand(round)
        self.event_phase(round)

    def play_round(self, round: str) -> None:
        """Control flow for a round"""
        for turn in turns:
            self.play_turn(round, turn)

    def play_game(self) -> None:
        """Control flow for a game"""
        for round in rounds:
            self.play_round(round)
