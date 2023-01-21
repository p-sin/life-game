import pytest
from unittest.mock import MagicMock

from life_game.play.game import Game
from life_game.setup.deal import deal_cards
from life_game.play.players import create_players, Player
from life_game.setup.components import rounds
from tests.utils import child_deal, adol_deal, adult_deal


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


@pytest.mark.parametrize(
    "round, hand_str, turn",
    [
        ("child", "child_hand", 1),
        ("child", "child_hand", 2),
        ("child", "child_hand", 3),
        ("child", "child_hand", 4),
        ("adol", "adol_hand", 1),
        ("adol", "adol_hand", 2),
        ("adol", "adol_hand", 3),
        ("adol", "adol_hand", 4),
        ("adult", "adult_hand", 1),
        ("adult", "adult_hand", 2),
        ("adult", "adult_hand", 3),
        ("adult", "adult_hand", 4),
    ],
)
def test_game_card_phase_hand(round, hand_str, turn) -> None:
    deals = deal_cards(6)
    players = create_players(6, deals)
    game = Game(6, players)
    game.card_phase(round, turn)

    for player, _ in players.items():
        hand = getattr(players[player], hand_str)
        assert list(hand.keys()) == [1, 2, 3, 4, 5, 6, 7]


@pytest.mark.parametrize(
    "round, turn",
    [
        ("child", 1),
        ("child", 2),
        ("child", 3),
        ("child", 4),
        ("adol", 1),
        ("adol", 2),
        ("adol", 3),
        ("adol", 4),
        ("adult", 1),
        ("adult", 2),
        ("adult", 3),
        ("adult", 4),
    ],
)
def test_game_card_phase_attributes(round, turn) -> None:
    deals = deal_cards(6)
    players = create_players(6, deals)
    game = Game(6, players)
    game.card_phase(round, turn)

    for player, _ in players.items():
        attribute_sum = 0

        for attribute_str in [
            "Sociability",
            "Intelligence",
            "Creativity",
            "Strength",
            "Constitution",
            "Coordination",
            "Empathy",
            "Determination",
        ]:
            attribute_sum += getattr(players[player].board, attribute_str)

        assert attribute_sum != 0


test_deals = {"child": child_deal, "adol": adol_deal, "adult": adult_deal}


@pytest.mark.parametrize(
    "player, out_hand",
    [
        (1, [46, 47, 48, 49, 50, 51, 52, 53, 54]),
        (2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (3, [10, 11, 12, 13, 14, 15, 16, 17, 18]),
        (4, [19, 20, 21, 22, 23, 24, 25, 26, 27]),
        (5, [28, 29, 30, 31, 32, 33, 34, 35, 36]),
        (6, [37, 38, 39, 40, 41, 42, 43, 44, 45]),
    ],
)
def test_pass_hand(player, out_hand) -> None:
    players = create_players(6, test_deals)
    game = Game(6, players)
    game.pass_hand("child")

    card_nums: list[int] = []

    for _, card in players[player].child_hand.items():
        card_nums.append(card["number"])

    assert card_nums == out_hand


def test_pass_event_phase():
    assert True


@pytest.mark.parametrize("function", [("card_phase"), ("pass_hand"), ("event_phase")])
def test_play_turn(function) -> None:
    players = create_players(6, test_deals)
    game = Game(6, players)
    setattr(game, function, MagicMock())
    game.play_turn("child", 1)
    assert getattr(game, function).called


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_play_round(round) -> None:
    players = create_players(6, test_deals)
    game = Game(6, players)
    game.play_turn = MagicMock()
    game.play_round(round)
    assert game.play_turn.call_count == 4


def test_game_play_game() -> None:
    players = create_players(6, test_deals)
    game = Game(6, players)
    game.play_round = MagicMock()
    game.play_game()
    assert game.play_round.call_count == 3
