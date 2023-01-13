import pytest
from life_game.setup.players import create_players, hand_type

from life_game.setup.components import Board
from life_game.setup.logic import Logic
from life_game.setup.deal import deal_cards

from typing import Union


@pytest.mark.parametrize(
    "total_players, outcome",
    [
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 2, 3]),
        (4, [1, 2, 3, 4]),
        (5, [1, 2, 3, 4, 5]),
        (6, [1, 2, 3, 4, 5, 6]),
    ],
)
def test_setup_player_info_count(total_players, outcome) -> None:
    """Test that the returned players object contains an entry for each expected player"""
    deals = deal_cards(total_players)
    players = create_players(total_players, deals)

    assert list(players.keys()) == outcome


@pytest.mark.parametrize(
    "element, type",
    [
        ("board", Board),
        ("logic", Logic),
        ("child_hand", dict),
        ("adol_hand", dict),
        ("adult_hand", dict),
    ],
)
def test_setup_player_info_type(element, type) -> None:
    """Test that each attribute of the Player class is the correct type"""
    deals = deal_cards(1)
    players = create_players(1, deals)

    assert isinstance(getattr(players[1], element), type)


# Test that no hand is the same
# Test contents of hands
