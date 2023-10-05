from unittest.mock import patch

import pytest

from life_game.components.constants import Attributes as A
from life_game.components.constants import BoardSlots as B
from life_game.setup.cards import Cards, attr_decks

card_config: dict[int, dict[str, B | list[A]]] = {
    1: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_TWO, A.NONE, A.NONE],
    },
    2: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.STRENGTH_TWO, A.CONST_TWO],
    },
}


def test_cards_initialization() -> None:
    with patch("life_game.setup.cards.card_config", card_config):
        cards = Cards()

        card_1 = cards.cards[1]
        card_2 = cards.cards[2]

        assert (
            card_1.board_slot == 1
            and card_1.sections[1].attr_slot == "attr_slot_1"
            and card_1.sections[1].attribute == "Sociability"
            and card_1.sections[1].value == 2
            and card_2.board_slot == 5
            and card_2.sections[2].attr_slot == "attr_slot_13"
            and card_2.sections[2].attribute == "Strength"
            and card_2.sections[2].value == 2
            and card_2.sections[3].attr_slot == "attr_slot_14"
            and card_2.sections[3].attribute == "Constitution"
            and card_2.sections[3].value == 2
        )


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_cards_deal_numbers_length(round: str) -> None:
    with patch("life_game.setup.cards.card_config", card_config):
        cards = Cards()

        assert len(cards.deal_numbers[round]) == 56


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_cards_deal_numbers(round: str) -> None:
    with patch("life_game.setup.cards.card_config", card_config):
        cards = Cards()

        print(cards.deal_numbers[round])
        print(attr_decks[round])

        assert all(card in attr_decks[round] for card in cards.deal_numbers[round])
