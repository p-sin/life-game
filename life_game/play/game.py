from dataclasses import dataclass

from life_game.components.components import ROUNDS, TURNS
from life_game.play.play_utils import card_num_start_end
from life_game.setup.cards import Cards
from life_game.setup.events import Events
from life_game.setup.players import Players


@dataclass
class Game:
    """Main control object. Contains all the components of the game
    and manages the control flow"""

    total_players: int
    players: Players
    cards: Cards
    events: Events

    def __post_init__(self) -> None:
        for round in ROUNDS:
            for player_num, player in self.players.players.items():
                start, end = card_num_start_end(player_num)
                card_nums = self.cards.deal_numbers[round][start:end]
                player_cards = {num: self.cards.cards[num] for num in card_nums}
                player.hand[round] = player_cards

    def card_phase(self) -> None:
        """The phase of each player choosing and playing cards
        and updating their board"""
        for _, player in self.players.players.items():
            player.choose_cards(self.round)
            player.play_cards()
            player.remove_cards(self.round)
            player.calculate_attribute_totals()

    def pass_hand(self) -> None:
        # Whoever the last player is, passes their card to a dummy player
        dummy_hand = self.players.players[self.total_players].hand[self.round]

        # Each player gets the hand of the player before them, except player 1
        for player in range(self.total_players, 1, -1):
            self.players.players[player].hand[self.round] = self.players.players[
                player - 1
            ].hand[self.round]

        # Player 1 then gets their hand from the dummy player
        # (originally the hand of the last player)
        self.players.players[1].hand[self.round] = dummy_hand

    def event_phase(self) -> None:
        """Control flow for the resolving of events"""
        for _, player in self.players.players.items():
            for _, event in self.events.events.items():
                player.points += event.resolve_event(player.board)

    def play_turn(self) -> None:
        """Control flow for a turn"""
        self.card_phase()
        self.pass_hand()
        self.event_phase()

    def play_round(self) -> None:
        """Control flow for a round"""
        for turn in TURNS:
            self.turn = turn
            self.play_turn()

    def play_game(self) -> None:
        """Control flow for a game"""
        for round in ROUNDS:
            self.round = round
            self.play_round()
