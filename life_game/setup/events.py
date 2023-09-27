import random
from dataclasses import dataclass, field

from pydantic import BaseModel

from life_game.components.components import ATTRIBUTES, ROUNDS, event_decks
from life_game.components.event_cards import event_cards
from life_game.setup.players import Board


@dataclass
class SingleCondition(BaseModel):
    attribute: str
    value: int

    def evaluate(self, board: Board) -> bool:
        return getattr(board, self.attribute) >= self.value


@dataclass
class MinCondition(BaseModel):
    attribute: list[str]
    total: int
    min: int

    def evaluate(self, board: Board) -> bool:
        total_value = 0

        for attribute in self.attribute:
            attr_value = getattr(board, attribute)
            total_value += attr_value if attr_value >= self.min else 0

        return total_value >= self.total


@dataclass
class MaxCondition(BaseModel):
    attribute: list[str]
    max_value: int

    def evaluate(self, board: Board) -> bool:
        for attribute in ATTRIBUTES:
            if getattr(board, attribute) > self.max_value:
                return False
        return True


@dataclass
class Outcome(BaseModel):
    flav_text: str
    points: int
    cond_type: str
    condition: SingleCondition | MinCondition | MaxCondition

    def check_condition(self, board: Board) -> bool:
        return self.condition.evaluate(board)


@dataclass
class Event:
    flav_text: str
    life_stage: str
    outcomes: dict[str, Outcome]

    def resolve_event(self, board: Board) -> int:
        final_points = 0

        for _, outcome in self.outcomes.items():
            if outcome.check_condition(board):
                if outcome.points > final_points:
                    final_points = outcome.points

        return final_points


@dataclass
class Events:
    events: dict[int, Event] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        for number, config in event_cards.items():
            event = Event(**config)  # type: ignore
            self.events[number] = event

    @property
    def deal_numbers(self) -> dict[str, list[int]]:
        return {round: random.sample(event_decks[round], 5) for round in ROUNDS}
