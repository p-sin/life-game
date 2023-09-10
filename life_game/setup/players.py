from dataclasses import dataclass, field

# from life_game.play.actions import Action
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
    attribute_slots: dict[int, AttributeSlot] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        self.attribute_slots = {number: AttributeSlot(number) for number in range(25)}


@dataclass
class Hand:
    hand: dict[int, Card]


@dataclass
class Player:
    """The player object defines each player in the game and holds all their
    information (board, cards, points, etc.)
    The methods in the player object are used to drive much of the activity in the game
    """

    board: Board = Board()
    points: int = 0
    child_hand: Hand = field(init=False)
    adol_hand: Hand = field(init=False)
    adult_hand: Hand = field(init=False)
    # action: Action = Action()
    # logic: Optional[Logic] = None


@dataclass
class Players:
    total_players: int
    players: dict[int, Player] = field(init=False, default_factory=dict)

    def __init__(self) -> None:
        self.players = {number: Player() for number in range(self.total_players)}
