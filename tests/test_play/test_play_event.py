import pytest

from typing import Tuple

from life_game.setup.components import Board, attribute_slots
from life_game.play.events import single_total
from life_game.setup.event_cards import event_cards, condition_type


def get_event_values(
    event_num: int, outcome_num: str
) -> Tuple[condition_type, str, int]:
    return (
        event_cards[event_num]["outcomes"][outcome_num]["condition"],
        event_cards[event_num]["outcomes"][outcome_num]["condition"]["attribute"],
        event_cards[event_num]["outcomes"][outcome_num]["condition"]["value"],
    )


@pytest.mark.parametrize(
    "event_num, outcome_num, outcome",
    [
        (1, "outcome_1", True),
        (2, "outcome_1", True),
        (27, "outcome_1", True),
        (29, "outcome_1", True),
        (40, "outcome_1", True),
        (3, "outcome_2", True),
        (4, "outcome_2", True),
        (30, "outcome_2", True),
        (31, "outcome_2", True),
        (41, "outcome_2", True),
        (1, "outcome_1", False),
        (2, "outcome_1", False),
        (27, "outcome_1", False),
        (29, "outcome_1", False),
        (40, "outcome_1", False),
        (3, "outcome_2", False),
        (4, "outcome_2", False),
        (30, "outcome_2", False),
        (31, "outcome_2", False),
        (41, "outcome_2", False),
    ],
)
def test_single_total_correct_eval(event_num, outcome_num, outcome) -> None:
    condition, attr, value = get_event_values(event_num, outcome_num)
    board = Board(attribute_slots)

    if outcome == True:
        setattr(board, attr, value)
    else:
        setattr(board, attr, 100)

    assert single_total(board, condition) == outcome
