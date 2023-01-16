import pytest
from life_game.setup.cards import cards


def test_card_number():
    """Test the correct number of cards have been defined"""
    assert len(cards) == 180


def test_board_section_number():
    """Test that each board section has the correct number of cards assigned to it"""

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

    actual_dict = {}

    for _, dict in cards.items():
        if dict["board_section"].value.number not in actual_dict.keys():
            actual_dict[dict["board_section"].value.number] = 0
        actual_dict[dict["board_section"].value.number] += 1

    assert actual_dict == expected_dict


@pytest.mark.parametrize(
    "card_slot, values",
    [
        (
            "card_slot_1",
            [
                "attr_slot_1",
                "attr_slot_4",
                "attr_slot_7",
                "attr_slot_9",
                "attr_slot_12",
                "attr_slot_15",
                "attr_slot_17",
                "attr_slot_20",
                "attr_slot_23",
            ],
        ),
        (
            "card_slot_2",
            [
                "attr_slot_2",
                "attr_slot_5",
                "attr_slot_8",
                "attr_slot_10",
                "attr_slot_13",
                "attr_slot_16",
                "attr_slot_18",
                "attr_slot_21",
                "attr_slot_24",
            ],
        ),
        (
            "card_slot_3",
            [
                "attr_slot_3",
                "attr_slot_6",
                "attr_slot_11",
                "attr_slot_14",
                "attr_slot_19",
                "attr_slot_22",
            ],
        ),
    ],
)
def test_card_slot_valid(card_slot: str, values: list[str]) -> None:
    """Test each card slot has a valid attribute slot assigned to it for that card slot"""

    for _, dict in cards.items():
        if dict[card_slot]["slot_number"] is None:
            assert True
        else:
            assert dict[card_slot]["slot_number"] in values


@pytest.mark.parametrize(
    "card_slot", [("card_slot_1"), ("card_slot_2"), ("card_slot_3")]
)
def test_board_section_match(card_slot: str) -> None:
    """Test that each card slot references the correct board section values as defined
    by its board_section value"""

    for _, dict in cards.items():
        if dict[card_slot]["slot_number"] is None:
            assert True
        else:
            assert (
                getattr(dict["board_section"].value, card_slot)
                == dict[card_slot]["slot_number"]
            )


def test_cards_by_attribute():
    """Test that all the defined cards contain the correct total of attribute values across
    the full set"""
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

    actual_dict = {}

    for _, dict in cards.items():
        if dict["card_slot_1"]["values"] is not None:
            if dict["card_slot_1"]["values"].value.name not in actual_dict.keys():
                actual_dict[dict["card_slot_1"]["values"].value.name] = 0
            actual_dict[dict["card_slot_1"]["values"].value.name] += dict[
                "card_slot_1"
            ]["values"].value.value

        if dict["card_slot_2"]["values"] is not None:
            if dict["card_slot_2"]["values"].value.name not in actual_dict.keys():
                actual_dict[dict["card_slot_2"]["values"].value.name] = 0
            actual_dict[dict["card_slot_2"]["values"].value.name] += dict[
                "card_slot_2"
            ]["values"].value.value

        if dict["card_slot_3"]["values"] is not None:
            if dict["card_slot_3"]["values"].value.name not in actual_dict.keys():
                actual_dict[dict["card_slot_3"]["values"].value.name] = 0
            actual_dict[dict["card_slot_3"]["values"].value.name] += dict[
                "card_slot_3"
            ]["values"].value.value

    assert actual_dict == expected_dict
