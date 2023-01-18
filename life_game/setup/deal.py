import random
from life_game.setup.components import decks, rounds
from life_game.setup.setup_exceptions import (
    InvalidPlayerCountRange,
    InvalidPlayerCountType,
)

deal_type = dict[str, list[int]]


def deal_cards(total_players: int) -> deal_type:
    if not isinstance(total_players, int):
        raise InvalidPlayerCountType(total_players)
    elif not 0 < total_players < 7:
        raise InvalidPlayerCountRange(total_players)
    else:
        deals = {}

        for round in rounds.keys():
            deal = random.sample(decks[round], total_players * 9)
            deals[round] = deal

        return deals
