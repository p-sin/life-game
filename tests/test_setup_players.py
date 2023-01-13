import pytest
from life_game.setup.players import setup_players

from life_game.setup.components import Board
from life_game.setup.logic import Logic

from typing import Union


@pytest.mark.parametrize(
    "player_num, outcome",
    [
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 2, 3]),
        (4, [1, 2, 3, 4]),
        (5, [1, 2, 3, 4, 5]),
        (6, [1, 2, 3, 4, 5, 6]),
    ],
)
def test_setup_player_count(
    player_num: int, outcome: Union[list[int], Exception]
) -> None:
    _, num_players = setup_players(player_num)

    assert num_players == outcome


def test_setup_player_info_count() -> None:
    game_space, _ = setup_players(3)

    assert list(game_space.player_info.keys()) == [1, 2, 3]


@pytest.mark.parametrize("element, type", [("board", Board), ("logic", Logic)])
def test_setup_player_info_type(element, type) -> None:
    game_space, _ = setup_players(1)

    assert isinstance(getattr(game_space.player_info[1], element), type)
