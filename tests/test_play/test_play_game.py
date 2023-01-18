import pytest

from life_game.play.game import Game
from life_game.setup.deal import deal_cards
from life_game.play.players import create_players, Player
from life_game.setup.components import rounds


# Test creation of game - structure
def test_game_creation_players() -> None:
    deals = deal_cards(1)
    players = create_players(1, deals)
    game = Game(players)
    assert isinstance(game.players[1], Player)


def test_game_card_phase_runs() -> None:
    try:
        deals = deal_cards(1)
        players = create_players(1, deals)
        game = Game(players)
        for round in rounds.keys():
            game.card_phase(round)
        assert True
    except:
        assert False


# Test card phase

# Test choose_cards (player)
# Test play_cards (player)
