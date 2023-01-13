import random
from life_game.setup.components import decks, rounds
from life_game.setup.cards import cards, card_type
from typing import Tuple
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

        for round in rounds:
            deal = random.sample(decks[round], total_players * 9)
            deals[round] = deal

        return deals


def select_player_cards(
    deals: dict[str, list[int]], player: int
) -> Tuple[dict[int, card_type], dict[int, card_type], dict[int, card_type]]:
    for round in rounds:
        start = 0 + (9 * (player - 1))
        end = 9 + (9 * (player - 1))
        player_deal = deals[round][start:end]

    player_cards: dict[str, dict[int, card_type]] = {}

    for num, card in enumerate(player_deal):
        player_cards[round][num + 1] = cards[card]

    return (player_cards["child"], player_cards["adol"], player_cards["adult"])
