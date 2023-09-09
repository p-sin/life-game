from life_game.setup.setup_exceptions import (
    InvalidPlayerCountRange,
    InvalidPlayerCountType,
)


def valid_players(total_players: int) -> bool:
    if not isinstance(total_players, int):
        raise InvalidPlayerCountType(total_players)
    elif not 0 < total_players < 7:
        raise InvalidPlayerCountRange(total_players)
    else:
        return True
