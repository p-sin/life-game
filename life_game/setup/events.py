import random
from dataclasses import dataclass, field
from typing import Literal

from pydantic import BaseModel

from life_game.components.components import ROUNDS, attr_decks, event_decks
from life_game.components.event_cards import event_cards


@dataclass
class SingleCondition(BaseModel):
    attribute: str
    value: int

    def check_condition(self) -> None:
        pass


@dataclass
class MinCondition(BaseModel):
    attribute: list[str]
    total: int
    min: int

    def check_condition(self) -> None:
        pass


@dataclass
class MaxCondition(BaseModel):
    attribute: list[str]
    max_value: int

    def check_condition(self) -> None:
        pass


@dataclass
class Outcome(BaseModel):
    flav_text: str
    points: int
    cond_type: str
    condition: SingleCondition | MinCondition | MaxCondition


@dataclass
class Event:
    flav_text: str
    life_stage: str
    outcomes: dict[str, Outcome]


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
