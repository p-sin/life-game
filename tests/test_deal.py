import pytest

from contextlib import nullcontext as does_not_raise
from life_game.setup.setup_exceptions import (
    InvalidPlayerCountRange,
    InvalidPlayerCountType,
)
from life_game.setup.deal import deal_cards


@pytest.mark.parametrize(
    "player_num, outcome",
    [
        (7, pytest.raises(InvalidPlayerCountRange)),
        (0, pytest.raises(InvalidPlayerCountRange)),
        (-1, pytest.raises(InvalidPlayerCountRange)),
        (5, does_not_raise()),
        ("text", pytest.raises(InvalidPlayerCountType)),
        (5.4, pytest.raises(InvalidPlayerCountType)),
        ([1, 2], pytest.raises(InvalidPlayerCountType)),
    ],
)
def test_setup_player_count_exceptions(player_num: int, outcome: Exception):
    """Test that invalid total_players values raise the correct exception"""
    with outcome:
        assert deal_cards(player_num)
