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
    curr_round: str = "child"

    def card_phase(self, turn: int):
        """ "The phase of each player choosing and playing cards and updating their board"""
        for _, player in self.players.items():
            chosen_cards, chosen_cards_pos = player.choose_cards(self.curr_round, turn)
            player.play_cards(chosen_cards)
            player.remove_cards(chosen_cards_pos, self.curr_round)
            player.calculate_attribute_totals()

    def pass_hand(self) -> None:
        """Passing each players hand on to the next player"""
        # Whoever the last player is, passes their card to a dummy player
        dummy_hand: hand_type = getattr(
            self.players[self.total_players], rounds[self.curr_round]
        )

        # Each player gets the hand of the player before them, except player 1
        for player in range(self.total_players, 1, -1):
            setattr(
                self.players[player],
                rounds[self.curr_round],
                getattr(self.players[player - 1], rounds[self.curr_round]),
            )

        # Player 1 then gets their hand from the dummy player (originally the hand of the last player)
        setattr(self.players[1], rounds[self.curr_round], dummy_hand)

    def select_events(self) -> None:
        pass

    def event_phase(self) -> None:
        events = self.select_events()
        for _, player in self.players.items():
            player.apply_events(events)

    def play_turn(self, turn: int) -> None:
        """Control flow for a turn"""
        self.card_phase(turn)
        self.pass_hand()
        self.event_phase()

    def play_round(self) -> None:
        """Control flow for a round"""
        for turn in turns:
            self.play_turn(turn)

    def play_game(self) -> None:
        """Control flow for a game"""
        for round in rounds:
            self.curr_round = round
            self.play_round()
