from typing import Any

import pytest

from life_game.components.attr_cards import card_config
from life_game.components.constants import Attributes as A
from life_game.components.constants import BoardSlots as B


def test_number_of_cards() -> None:
    """Test the correct number of cards have been defined"""
    assert len(card_config) == 180


def test_board_slot_number() -> None:
    """Test that each board slot has the correct number of cards assigned to it"""

    expected_dict = {
        1: 27,
        2: 27,
        3: 6,
        4: 27,
        5: 27,
        6: 6,
        7: 27,
        8: 27,
        9: 6,
    }

    actual_dict: dict[Any, Any] = {board_section: 0 for board_section in range(1, 10)}

    for card in card_config.values():
        slot: B = card["board_slot"].value.number  # type: ignore
        actual_dict[slot] += 1

    assert actual_dict == expected_dict


def test_board_slot_attributes_valid() -> None:
    """Test each board slot contains valid attributes"""

    exp_attributes: dict[int, list[A]] = {
        1: [
            A.SOCIAL_ONE,
            A.SOCIAL_TWO,
            A.INTEL_ONE,
            A.INTEL_TWO,
            A.CREATE_ONE,
            A.CREATE_TWO,
        ],
        2: [
            A.STRENGTH_ONE,
            A.STRENGTH_TWO,
            A.CONST_ONE,
            A.CONST_TWO,
            A.COORD_ONE,
            A.COORD_TWO,
        ],
        3: [
            A.EMPATHY_ONE,
            A.EMPATHY_TWO,
            A.DETERM_ONE,
            A.DETERM_TWO,
        ],
        4: [
            A.SOCIAL_THREE,
            A.SOCIAL_TWO,
            A.INTEL_THREE,
            A.INTEL_TWO,
            A.CREATE_THREE,
            A.CREATE_TWO,
        ],
        5: [
            A.STRENGTH_THREE,
            A.STRENGTH_TWO,
            A.CONST_THREE,
            A.CONST_TWO,
            A.COORD_THREE,
            A.COORD_TWO,
        ],
        6: [
            A.EMPATHY_THREE,
            A.EMPATHY_TWO,
            A.DETERM_THREE,
            A.DETERM_TWO,
        ],
        7: [
            A.SOCIAL_FOUR,
            A.SOCIAL_TWO,
            A.INTEL_FOUR,
            A.INTEL_TWO,
            A.CREATE_FOUR,
            A.CREATE_TWO,
        ],
        8: [
            A.STRENGTH_FOUR,
            A.STRENGTH_TWO,
            A.CONST_FOUR,
            A.CONST_TWO,
            A.COORD_FOUR,
            A.COORD_TWO,
        ],
        9: [
            A.EMPATHY_FOUR,
            A.EMPATHY_TWO,
            A.DETERM_FOUR,
            A.DETERM_TWO,
        ],
    }

    for card in card_config.values():
        values: list[A] = card["values"]  # type: ignore
        for value in values:
            if value.value.name == "":
                assert True
            else:
                assert value in (
                    exp_attributes[card["board_slot"].value.number]  # type: ignore
                )


def test_cards_by_attribute_occurence() -> None:
    """Test that all the defined cards contain the correct total of attribute values
    across the full set"""
    expected_dict = {
        "Sociability": 87,
        "Intelligence": 87,
        "Creativity": 87,
        "Strength": 87,
        "Constitution": 87,
        "Coordination": 87,
        "Empathy": 28,
        "Determination": 28,
    }

    actual_dict: dict[Any, Any] = {
        "Sociability": 0,
        "Intelligence": 0,
        "Creativity": 0,
        "Strength": 0,
        "Constitution": 0,
        "Coordination": 0,
        "Empathy": 0,
        "Determination": 0,
    }

    for card in card_config.values():
        attributes: list[A] = card["values"]  # type: ignore

        for attribute in attributes:
            if attribute.value.name != "":
                actual_dict[attribute.value.name] += attribute.value.value
    assert actual_dict == expected_dict
