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
        (1, does_not_raise()),
        (2, does_not_raise()),
        (3, does_not_raise()),
        (4, does_not_raise()),
        (5, does_not_raise()),
        (6, does_not_raise()),
        ("text", pytest.raises(InvalidPlayerCountType)),
        (5.4, pytest.raises(InvalidPlayerCountType)),
        ([1, 2], pytest.raises(InvalidPlayerCountType)),
    ],
)
def test_total_player_count_exceptions(player_num: int, outcome: Exception):
    """Test that invalid total_players values raise the correct exception"""
    with outcome:
        assert deal_cards(player_num)


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_deal_correct_rounds(round):
    """Test that the deal function generates a deal for each round"""
    deals = deal_cards(6)
    assert round in deals


@pytest.mark.parametrize(
    "round, total_players, num_cards",
    [
        ("child", 1, 9),
        ("adol", 1, 9),
        ("adult", 1, 9),
        ("child", 2, 18),
        ("adol", 2, 18),
        ("adult", 2, 18),
        ("child", 3, 27),
        ("adol", 3, 27),
        ("adult", 3, 27),
        ("child", 4, 36),
        ("adol", 4, 36),
        ("adult", 4, 36),
        ("child", 5, 45),
        ("adol", 5, 45),
        ("adult", 5, 45),
        ("child", 6, 54),
        ("adol", 6, 54),
        ("adult", 6, 54),
    ],
)
def test_deal_correct_num_cards(round, total_players, num_cards):
    """Test that the deal function generates the correct number of card numbers
    for the player count"""
    deals = deal_cards(total_players)
    assert len(deals[round]) == num_cards
