from typing import List, Union

import pytest

from life_game.components.event_cards import event_cards


def test_number_of_events() -> None:
    """Test the correct number of cards have been defined"""
    assert len(event_cards) == 84


@pytest.mark.parametrize("stage", [("child"), ("adol"), ("adult")])
def test_number_events_per_stage(stage: str) -> None:
    """Test that the event cards are correctly distrubted across
    the three life stages"""

    stage_count = sum(
        1 for event in event_cards.values() if event["life_stage"] == stage
    )
    assert stage_count == 28


def test_attributes_appear_exp_amount() -> None:
    """Test that attributes appear in the event cards the
    expected number of times"""

    exp_amount = {
        "Sociability": 42,
        "Intelligence": 42,
        "Creativity": 42,
        "Strength": 42,
        "Constitution": 42,
        "Coordination": 42,
        "Empathy": 42,
        "Determination": 42,
    }

    act_amount = {attribute: 0 for attribute in exp_amount.keys()}

    for event in event_cards.values():
        for outcome in event["outcomes"].values():  # type: ignore
            if outcome["type"] != "max":
                attributes: Union[str, List[str]] = outcome["condition"][
                    "attribute"  # type: ignore
                ]
                if isinstance(attributes, list):
                    for attribute in attributes:
                        act_amount[attribute] += 1
                else:
                    act_amount[attributes] += 1

    assert act_amount == exp_amount


def test_points_correct() -> None:
    """Tests that the points for each outcome match the life
    stage and type of outcome"""

    points_map: dict[str, dict[str, int]] = {
        "child": {"single": 1, "min": 3},
        "adol": {"single": 3, "min": 3},
        "adult": {"single": 5, "min": 5},
    }

    for event in event_cards.values():
        for outcome in event["outcomes"].values():  # type: ignore
            assert outcome["points"] == points_map[event["life_stage"]]  # type: ignore
            [outcome["type"]]


@pytest.mark.parametrize("outcome_type, exp_amount", [("single", 168), ("min", 84)])
def test_occurence_types(outcome_type: str, exp_amount: int) -> None:
    """Test that each occurence type occurs the expected number
    of times"""
    count = sum(
        1  # type: ignore
        for event in event_cards.values()
        for outcome in event["outcomes"].values()  # type: ignore
        if outcome["type"] == outcome_type
    )
    assert count == exp_amount


def test_condition_values_req() -> None:
    """Tests that the value threshold for each test is as expected"""

    values_map: dict[str, dict[str, Union[int, list[int]]]] = {
        "child": {"single": 2, "min": [4, 1]},
        "adol": {"single": 5, "min": [7, 3]},
        "adult": {"single": 8, "min": [10, 6]},
    }

    for event in event_cards.values():
        for outcome in event["outcomes"].values():  # type: ignore
            if outcome["type"] == "single":
                assert (
                    outcome["condition"]["value"]  # type: ignore
                    == values_map[event["life_stage"]][outcome["type"]]  # type: ignore
                )
            else:
                assert (
                    outcome["condition"]["total"]  # type: ignore
                    == values_map[event["life_stage"]][outcome["type"]][0]  # type: ignore
                    and outcome["condition"]["min"]  # type: ignore
                    == values_map[event["life_stage"]][outcome["type"]][1]  # type: ignore
                )
