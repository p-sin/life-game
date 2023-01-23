import random
from life_game.setup.components import attr_decks, event_decks, rounds
from life_game.setup.event_cards import event_cards, event_type

deal_type = dict[str, list[int]]


def deal_cards(total_players: int) -> deal_type:
    """Randomly take 9 * number of players integers from the deck of cards for each round.
    This will provide 9 cards for each player"""
    deals = {}

    for round in rounds.keys():
        deal = random.sample(attr_decks[round], total_players * 9)
        deals[round] = deal

    return deals


def deal_events() -> dict[str, dict[int, event_type]]:
    """Randomly select 5 numbers from each of the event decks ?(one for each round)"""
    events = {}
    for round in rounds.keys():
        round_events = {}
        event_deal = random.sample(event_decks[round], 5)
        for num, event in enumerate(event_deal):
            round_events[num] = event_cards[event]
        events[round] = round_events

    return events
