import random
from dataclasses import dataclass, field

from life_game.components.attr_cards import card_config
from life_game.components.components import ROUNDS, attr_decks


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
            card = Card(
                board_slot=config["board_slot"].value.number,  # type: ignore
                sections={
                    1: CardStat(
                        attr_slot=config["board_slot"].value.card_slot_1,  # type: ignore
                        attribute=config["values"][0].value.name,  # type: ignore
                        value=config["values"][0].value.value,  # type: ignore
                    ),
                    2: CardStat(
                        attr_slot=config["board_slot"].value.card_slot_2,  # type: ignore
                        attribute=config["values"][2].value.name,  # type: ignore
                        value=config["values"][2].value.value,  # type: ignore
                    ),
                    3: CardStat(
                        attr_slot=config["board_slot"].value.card_slot_3,  # type: ignore
                        attribute=config["values"][2].value.name,  # type: ignore
                        value=config["values"][2].value.value,  # type: ignore
                    ),
                },
            )

            self.cards[number] = card

    @property
    def deal_numbers(self) -> dict[str, list[int]]:
        return {round: random.sample(attr_decks[round], 56) for round in ROUNDS}
