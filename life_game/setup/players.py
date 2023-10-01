import random
from dataclasses import dataclass, field

from life_game.components.constants import ATTRIBUTES
from life_game.setup.cards import Card


@dataclass
class AttributeSlot:
    number: int
    name: str = ""
    value: int = 0


@dataclass
class Board:
    """Defines the playerboard"""

    Sociability: int = 0
    Intelligence: int = 0
    Creativity: int = 0
    Strength: int = 0
    Constitution: int = 0
    Coordination: int = 0
    Empathy: int = 0
    Determination: int = 0
    attr_slots: dict[int, AttributeSlot] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        self.attr_slots = {number: AttributeSlot(number) for number in range(25)}


@dataclass
class Player:
    """The player object defines each player in the game and holds all their
    information (board, cards, points, etc.)
    The methods in the player object are used to drive much of the activity in the game
    """

    points: int = 0
    hand: dict[str, dict[int, Card]] = field(init=False, default_factory=dict)
    board: Board = field(init=False)
    # logic: Optional[Logic] = None

    def __post_init__(self) -> None:
        self.board = Board()

    def choose_cards(self, round: str) -> None:
        self.chosen_cards_num = random.sample(list(self.hand[round]), 2)
        self.chosen_cards = [self.hand[round][num] for num in self.chosen_cards_num]

    def play_cards(self) -> None:
        for card in self.chosen_cards:
            for _, stat in card.sections.items():
                if stat.attribute is not None:
                    self.board.attr_slots[stat.attr_slot].name = stat.attribute
                    self.board.attr_slots[stat.attr_slot].value = stat.value

    def remove_cards(self, round: str) -> None:
        for card in self.chosen_cards_num:
            del self.hand[round][card]

    def calculate_attribute_totals(self) -> None:
        for attribute in ATTRIBUTES:
            value = 0
            for _, slot in self.board.attr_slots.items():
                if attribute == slot.name:
                    value += slot.value

            setattr(self.board, attribute, value)


@dataclass
class Players:
    total_players: int
    players: dict[int, Player] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        self.players = {number: Player() for number in range(self.total_players)}
