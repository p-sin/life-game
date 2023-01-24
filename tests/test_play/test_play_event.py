import pytest

from typing import Tuple, Union

from life_game.setup.components import Board, attribute_slots
from life_game.play.events import single_total, min_total, max_value
from life_game.setup.event_cards import event_cards, condition_type


def get_event_values(
    event_num: int, outcome_num: str
) -> Tuple[condition_type, Union[str, list[str]]]:
    return (
        event_cards[event_num]["outcomes"][outcome_num]["condition"],
        event_cards[event_num]["outcomes"][outcome_num]["condition"]["attribute"],
    )


@pytest.mark.parametrize(
    "event_num, outcome_num, value, outcome",
    [
        (1, "outcome_1", 2, True),
        (2, "outcome_1", 3, True),
        (27, "outcome_1", 4, True),
        (29, "outcome_1", 50, True),
        (40, "outcome_1", 1000, True),
        (3, "outcome_2", 2, True),
        (4, "outcome_2", 3, True),
        (30, "outcome_2", 4, True),
        (31, "outcome_2", 50, True),
        (41, "outcome_2", 1000, True),
        (1, "outcome_1", 0, False),
        (2, "outcome_1", 0, False),
        (27, "outcome_1", 0, False),
        (29, "outcome_1", 0, False),
        (40, "outcome_1", 0, False),
        (3, "outcome_2", 0, False),
        (4, "outcome_2", 0, False),
        (30, "outcome_2", 0, False),
        (31, "outcome_2", 0, False),
        (41, "outcome_2", 0, False),
    ],
)
def test_single_total_correct_eval(event_num, outcome_num, value, outcome) -> None:
    condition, attr = get_event_values(event_num, outcome_num)
    board = Board(attribute_slots)

    setattr(board, attr, value)

    assert single_total(board, condition) == outcome


@pytest.mark.parametrize(
    "event_num, outcome_num, value_1, value_2, outcome",
    [
        (1, "outcome_3", 3, 1, True),
        (2, "outcome_3", 1, 3, True),
        (3, "outcome_3", 4, 5, True),
        (27, "outcome_3", 10, 2, True),
        (29, "outcome_3", 16, 12, True),
        (40, "outcome_3", 50, 2, True),
        (41, "outcome_3", 50, 23, True),
        (3, "outcome_3", 1, 1, False),
        (4, "outcome_3", 6, 0, False),
        (30, "outcome_3", 0, 0, False),
        (31, "outcome_3", 9, 1, False),
        (40, "outcome_3", 0, 6, False),
        (41, "outcome_3", 23, 1, False),
    ],
)
def test_min_total_correct_eval(
    event_num, outcome_num, value_1, value_2, outcome
) -> None:
    condition, attr = get_event_values(event_num, outcome_num)
    board = Board(attribute_slots)

    setattr(board, attr[0], value_1)
    setattr(board, attr[1], value_2)

    assert min_total(board, condition) == outcome


def get_max_event_values(event_num: int, outcome_num: str) -> condition_type:
    return event_cards[event_num]["outcomes"][outcome_num]["condition"]


@pytest.mark.parametrize(
    "event_num, outcome_num, value, outcome",
    [
        (21, "outcome_1", 2, True),
        (21, "outcome_1", 1, True),
        (21, "outcome_2", 1, True),
        (21, "outcome_2", 0, True),
        (42, "outcome_1", 4, True),
        (42, "outcome_1", 3, True),
        (42, "outcome_2", 2, True),
        (42, "outcome_2", 1, True),
        (63, "outcome_1", 6, True),
        (63, "outcome_1", 4, True),
        (63, "outcome_2", 2, True),
        (63, "outcome_2", 1, True),
        (21, "outcome_1", 10, False),
        (21, "outcome_1", 10, False),
        (21, "outcome_2", 10, False),
        (21, "outcome_2", 10, False),
        (42, "outcome_1", 10, False),
        (42, "outcome_1", 10, False),
        (42, "outcome_2", 10, False),
        (42, "outcome_2", 10, False),
        (63, "outcome_1", 10, False),
        (63, "outcome_1", 10, False),
        (63, "outcome_2", 10, False),
        (63, "outcome_2", 10, False),
    ],
)
def test_max_value_correct_eval(event_num, outcome_num, value, outcome) -> None:
    condition = get_max_event_values(event_num, outcome_num)

    board = Board(attribute_slots)
    board.Constitution = value
    board.Coordination = value
    board.Creativity = value
    board.Determination = value
    board.Empathy = value
    board.Intelligence = value
    board.Sociability = value
    board.Strength = value

    assert max_value(board, condition) == outcome


def test_resolve_event_correct_map() -> None:

def test_resolve_event_correct_points() -> None: