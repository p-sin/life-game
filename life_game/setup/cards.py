import random
from dataclasses import dataclass, field

from life_game.components.attr_cards import card_config
from life_game.components.components import ROUNDS, attr_decks


@dataclass
class CardStat:
    attribute_slot: int
    attribute: str
    value: int


@dataclass
class Card:
    board_slot: int
    section_1: CardStat
    section_2: CardStat
    section_3: CardStat


@dataclass
class Cards:
    cards: dict[int, Card] = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        for number, config in card_config.items():
            card = Card(
                board_slot=config["board_slot"].value.number,  # type: ignore
                section_1=CardStat(
                    attribute_slot=config["board_slot"].value.card_slot_1,  # type: ignore
                    attribute=config["values"][0].value.name,  # type: ignore
                    value=config["values"][0].value.value,  # type: ignore
                ),
                section_2=CardStat(
                    attribute_slot=config["board_slot"].value.card_slot_2,  # type: ignore
                    attribute=config["values"][2].value.name,  # type: ignore
                    value=config["values"][2].value.value,  # type: ignore
                ),
                section_3=CardStat(
                    attribute_slot=config["board_slot"].value.card_slot_3,  # type: ignore
                    attribute=config["values"][2].value.name,  # type: ignore
                    value=config["values"][2].value.value,  # type: ignore
                ),
            )

            self.cards[number] = card

    @property
    def deal_numbers(self) -> dict[str, list[int]]:
        return {round: random.sample(attr_decks[round], 56) for round in ROUNDS}
