import random
from life_game.setup.components import decks, rounds

deal_type = dict[str, list[int]]


def deal_cards(total_players: int) -> deal_type:
    """Randomly take 9 * number of players integers from the deck of cards for each round.
    This will provide 9 cards for each player"""
    deals = {}

    for round in rounds.keys():
        deal = random.sample(decks[round], total_players * 9)
        deals[round] = deal

    return deals
