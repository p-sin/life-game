import json
from typing import Any, Optional

import pytest

from life_game.components import constants as c
from life_game.components.attr_cards import card_config
from life_game.paths import Paths


def test_rounds() -> None:
    assert c.ROUNDS == {
        "child": "child_hand",
        "adol": "adol_hand",
        "adult": "adult_hand",
    }


def test_turns() -> None:
    assert c.TURNS == [1, 2, 3, 4]


def test_attributes() -> None:
    assert c.ATTRIBUTES == [
        "Sociability",
        "Intelligence",
        "Creativity",
        "Strength",
        "Constitution",
        "Coordination",
        "Empathy",
        "Determination",
    ]


@pytest.mark.parametrize(
    "enum, name, value",
    [
        ("NONE", "", 0),
        ("SOCIAL_ONE", "Sociability", 1),
        ("SOCIAL_TWO", "Sociability", 2),
        ("SOCIAL_THREE", "Sociability", 3),
        ("SOCIAL_FOUR", "Sociability", 4),
        ("INTEL_ONE", "Intelligence", 1),
        ("INTEL_TWO", "Intelligence", 2),
        ("INTEL_THREE", "Intelligence", 3),
        ("INTEL_FOUR", "Intelligence", 4),
        ("CREATE_ONE", "Creativity", 1),
        ("CREATE_TWO", "Creativity", 2),
        ("CREATE_THREE", "Creativity", 3),
        ("CREATE_FOUR", "Creativity", 4),
        ("STRENGTH_ONE", "Strength", 1),
        ("STRENGTH_TWO", "Strength", 2),
        ("STRENGTH_THREE", "Strength", 3),
        ("STRENGTH_FOUR", "Strength", 4),
        ("CONST_ONE", "Constitution", 1),
        ("CONST_TWO", "Constitution", 2),
        ("CONST_THREE", "Constitution", 3),
        ("CONST_FOUR", "Constitution", 4),
        ("COORD_ONE", "Coordination", 1),
        ("COORD_TWO", "Coordination", 2),
        ("COORD_THREE", "Coordination", 3),
        ("COORD_FOUR", "Coordination", 4),
        ("EMPATHY_ONE", "Empathy", 1),
        ("EMPATHY_TWO", "Empathy", 2),
        ("EMPATHY_THREE", "Empathy", 3),
        ("EMPATHY_FOUR", "Empathy", 4),
        ("DETERM_ONE", "Determination", 1),
        ("DETERM_TWO", "Determination", 2),
        ("DETERM_THREE", "Determination", 3),
        ("DETERM_FOUR", "Determination", 4),
    ],
)
def test_attributes_enum(enum: str, name: str, value: int) -> None:
    """Test that the Attributes Enum is correct"""
    try:
        assert (
            c.Attributes[enum].value.name == name
            and c.Attributes[enum].value.value == value
        )
    except Exception:
        assert False


@pytest.mark.parametrize(
    "enum, number, body, stage, slot_1, slot_2, slot_3",
    [
        (
            "BOARD_SLOT_ONE",
            1,
            "mind",
            "child",
            "attr_slot_1",
            "attr_slot_2",
            "attr_slot_3",
        ),
        (
            "BOARD_SLOT_TWO",
            2,
            "body",
            "child",
            "attr_slot_4",
            "attr_slot_5",
            "attr_slot_6",
        ),
        ("BOARD_SLOT_THREE", 3, "soul", "child", "attr_slot_7", "attr_slot_8", None),
        (
            "BOARD_SLOT_FOUR",
            4,
            "mind",
            "adol",
            "attr_slot_9",
            "attr_slot_10",
            "attr_slot_11",
        ),
        (
            "BOARD_SLOT_FIVE",
            5,
            "body",
            "adol",
            "attr_slot_12",
            "attr_slot_13",
            "attr_slot_14",
        ),
        (
            "BOARD_SLOT_SIX",
            6,
            "soul",
            "adol",
            "attr_slot_15",
            "attr_slot_16",
            None,
        ),
        (
            "BOARD_SLOT_SEVEN",
            7,
            "mind",
            "adult",
            "attr_slot_17",
            "attr_slot_18",
            "attr_slot_19",
        ),
        (
            "BOARD_SLOT_EIGHT",
            8,
            "body",
            "adult",
            "attr_slot_20",
            "attr_slot_21",
            "attr_slot_22",
        ),
        (
            "BOARD_SLOT_NINE",
            9,
            "soul",
            "adult",
            "attr_slot_23",
            "attr_slot_24",
            None,
        ),
    ],
)
def test_body_slot_enum_defined(
    enum: str,
    number: int,
    body: str,
    stage: str,
    slot_1: str,
    slot_2: str,
    slot_3: Optional[str],
) -> None:
    """Test that the BoardSection enum is correct"""
    try:
        assert (
            c.BoardSlots[enum].value.number == number
            and c.BoardSlots[enum].value.body_part == body
            and c.BoardSlots[enum].value.life_stage == stage
            and c.BoardSlots[enum].value.card_slot_1 == slot_1
            and c.BoardSlots[enum].value.card_slot_2 == slot_2
            and c.BoardSlots[enum].value.card_slot_3 == slot_3
        )
    except Exception:
        assert False


@pytest.mark.parametrize("stage", [("child"), ("adol"), ("adult")])
def test_num_cards_in_deck(stage: str) -> None:
    assert len(c.attr_decks[stage]) == 80


@pytest.mark.parametrize(
    "stage, total",
    [
        ("child", 2864),
        ("adol", 7664),
        ("adult", 12464),
    ],
)
def test_correct_cards_in_deck(stage: str, total: int) -> None:
    """Test that each deck contains the expected total number of
    card IDs"""
    assert sum(c.attr_decks[stage]) == total


def test_deck_by_attribute() -> None:
    """Test that the cards contained in each deck are correct by extracting the value
    of each attribute contained on the card"""
    expected_dict = {
        "Sociability": 87,
        "Intelligence": 87,
        "Creativity": 87,
        "Strength": 87,
        "Constitution": 87,
        "Coordination": 87,
        "Empathy": 126,
        "Determination": 126,
    }

    actual_dict = {
        "Sociability": 0,
        "Intelligence": 0,
        "Creativity": 0,
        "Strength": 0,
        "Constitution": 0,
        "Coordination": 0,
        "Empathy": 0,
        "Determination": 0,
    }

    deck = c.attr_decks["child"] + c.attr_decks["adol"] + c.attr_decks["adult"]

    for card_num in deck:
        card = card_config[card_num]

        if card["values"][0].value.value != 0:  # type: ignore
            actual_dict[card["values"][0].value.name] += card["values"][  # type: ignore
                0
            ].value.value

        if card["values"][1].value.value != 0:  # type: ignore
            actual_dict[card["values"][1].value.name] += card["values"][  # type: ignore
                1
            ].value.value

        if card["values"][2].value.value != 0:  # type: ignore
            actual_dict[card["values"][2].value.name] += card["values"][  # type: ignore
                2
            ].value.value

    assert actual_dict == expected_dict


@pytest.mark.parametrize("stage", [("child"), ("adol"), ("adult")])
def test_num_events_in_deck(stage: str) -> None:
    assert len(c.event_decks[stage]) == 28


@pytest.mark.parametrize(
    "stage, total", [("child", 406), ("adol", 1190), ("adult", 1974)]
)
def test_correct_events_in_deck(stage: str, total: int) -> None:
    """Test the total of each card number is correct for each stage"""
    assert sum(c.event_decks[stage]) == total


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_event_deck_correct_round(round: str) -> None:
    """Test that each event deck has only cards belonging to that round"""
    with open(Paths.EVENT_CARDS, mode="r", encoding="utf-8") as f:
        events = json.load(f)

    for card_num in c.event_decks[round]:
        assert events[str(card_num)]["life_stage"] == round
