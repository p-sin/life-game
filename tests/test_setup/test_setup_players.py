import pytest
from life_game.play.players import (
    create_players,
    select_player_cards,
    select_player_deal,
)

from life_game.setup.components import Board
from life_game.setup.logic import Logic
from life_game.setup.deal import deal_cards
from tests.utils import child_deal, adol_deal, adult_deal


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


@pytest.mark.parametrize(
    "player, round, hand",
    [
        (1, "child", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (1, "adol", [28, 29, 30, 31, 32, 33, 34, 35, 36]),
        (1, "adult", [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        (2, "child", [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        (2, "adol", [37, 38, 39, 40, 41, 42, 43, 44, 45]),
        (2, "adult", [19, 20, 21, 22, 23, 24, 25, 26, 27]),
        (3, "child", [19, 20, 21, 22, 23, 24, 25, 26, 27]),
        (3, "adol", [46, 47, 48, 49, 50, 51, 52, 53, 54]),
        (3, "adult", [28, 29, 30, 31, 32, 33, 34, 35, 36]),
        (4, "child", [28, 29, 30, 31, 32, 33, 34, 35, 36]),
        (4, "adol", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (4, "adult", [37, 38, 39, 40, 41, 42, 43, 44, 45]),
        (5, "child", [37, 38, 39, 40, 41, 42, 43, 44, 45]),
        (5, "adol", [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        (5, "adult", [46, 47, 48, 49, 50, 51, 52, 53, 54]),
        (6, "child", [46, 47, 48, 49, 50, 51, 52, 53, 54]),
        (6, "adol", [19, 20, 21, 22, 23, 24, 25, 26, 27]),
        (6, "adult", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ],
)
def test_player_deal(player, round, hand) -> None:
    """Tests that the deals object is correctly sliced for each player"""
    deals = {"child": child_deal, "adol": adol_deal, "adult": adult_deal}
    out_hand = select_player_deal(deals, player, round)

    assert out_hand == hand


player_card_deals = {
    "child": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    "adol": [10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "adult": [19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9],
}


@pytest.mark.parametrize(
    "round, player, numbers",
    [
        ("child", 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ("adol", 1, [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        ("adult", 1, [19, 20, 21, 22, 23, 24, 25, 26, 27]),
        ("child", 2, [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        ("adol", 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ("adult", 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ],
)
def test_select_player_cards(round, player, numbers) -> None:
    """Test that each player has the correct card objects in their hand by checking the number of the
    card"""
    child_hand, adol_hand, adult_hand = select_player_cards(player_card_deals, player)

    test_dict = {
        "child": child_hand,
        "adol": adol_hand,
        "adult": adult_hand,
    }

    card_nums = []
    for x in range(9):
        card_nums.append(test_dict[round][x + 1]["number"])

    assert card_nums == numbers
