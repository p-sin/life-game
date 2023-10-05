import random
from dataclasses import dataclass, field

from life_game.components.attr_cards import card_config
from life_game.components.constants import ROUNDS, attr_decks


@dataclass
class CardStat:
    attr_slot: int
    attribute: str
    value: int


@dataclass
class Card:
    board_slot: int
    sections: dict[int, CardStat]


@dataclass
class Cards:
    cards: dict[int, Card] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        for number, config in card_config.items():
            board_slot = config["board_slot"].value  # type: ignore

            sections = {
                i
                + 1: CardStat(
                    attr_slot=getattr(board_slot, f"card_slot_{i + 1}"),  # type: ignore
                    attribute=config["values"][i].value.name,  # type: ignore
                    value=config["values"][i].value.value,  # type: ignore
                )
                for i in range(3)
            }

            self.cards[number] = Card(board_slot=board_slot.number, sections=sections)

    @property
    def deal_numbers(self) -> dict[str, list[int]]:
        return {round: random.sample(attr_decks[round], 56) for round in ROUNDS}
