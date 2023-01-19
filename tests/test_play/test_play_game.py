import pytest

from life_game.play.game import Game
from life_game.setup.deal import deal_cards
from life_game.play.players import create_players, Player
from life_game.setup.components import rounds


@pytest.mark.parametrize("component, type", [("total_players", int)])
def test_game_creation_structure(component, type) -> None:
    deals = deal_cards(1)
    players = create_players(1, deals)
    game = Game(1, players)
    assert isinstance(getattr(game, component), type)


def test_game_creation_player_structure() -> None:
    deals = deal_cards(1)
    players = create_players(1, deals)
    game = Game(1, players)
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
