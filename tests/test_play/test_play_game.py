import pytest
from unittest.mock import MagicMock

from main import valid_players
from life_game.play.game import Game
from life_game.setup.deal import deal_cards, deal_events
from life_game.play.players import create_players, Player
from tests.utils import child_deal, adol_deal, adult_deal
from life_game.setup.setup_exceptions import (
    InvalidPlayerCountRange,
    InvalidPlayerCountType,
)
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "player_num, outcome",
    [
        (7, pytest.raises(InvalidPlayerCountRange)),
        (0, pytest.raises(InvalidPlayerCountRange)),
        (-1, pytest.raises(InvalidPlayerCountRange)),
        (1, does_not_raise()),
        (2, does_not_raise()),
        (3, does_not_raise()),
        (4, does_not_raise()),
        (5, does_not_raise()),
        (6, does_not_raise()),
        ("text", pytest.raises(InvalidPlayerCountType)),
        (5.4, pytest.raises(InvalidPlayerCountType)),
        ([1, 2], pytest.raises(InvalidPlayerCountType)),
    ],
)
def test_total_player_count_exceptions(player_num: int, outcome: Exception):
    """Test that invalid total_players values raise the correct exception"""
    with outcome:
        assert valid_players(player_num)


@pytest.mark.parametrize(
    "component, type", [("total_players", int), ("curr_round", str)]
)
def test_game_creation_structure(component, type) -> None:
    """Tests that the Game object has the correct structure"""
    deals = deal_cards(1)
    players = create_players(1, deals)
    events = deal_events()
    game = Game(1, players, events)
    assert isinstance(getattr(game, component), type)


def test_game_creation_player_structure() -> None:
    """Tests that the player object inside the game is the correct object"""
    deals = deal_cards(1)
    players = create_players(1, deals)
    events = deal_events()
    game = Game(1, players, events)
    assert isinstance(game.players[1], Player)


def test_game_creation_event_structure() -> None:
    """Tests that the event object inside the game is the correct object"""
    deals = deal_cards(1)
    players = create_players(1, deals)
    events = deal_events()
    game = Game(1, players, events)

    assert isinstance(game.events["child"][1]["flav_text"], str)


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
    """Tests that the card phase method runs correctly by checking that 2 cards have been removed
    from the player hand (shows the remove_cards process was called). Does not need to test further
    as the individual method has already been tested"""
    deals = deal_cards(6)
    players = create_players(6, deals)
    game = Game(6, players, {})
    game.curr_round = round
    game.card_phase(turn)

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
    """Tests that the card phase method runs correctly by checking that no player has 0 for all of their
    attributes. Shows the updating of the attributes process was called. Does not need to test further
    as the individual method has already been tested"""
    deals = deal_cards(6)
    players = create_players(6, deals)
    game = Game(6, players, {})
    game.curr_round = round
    game.card_phase(turn)

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
    """Tests the pass_hand method runs corectly by checking that each player has the expected (switched)
    hand."""
    players = create_players(6, test_deals)
    events = deal_events()
    game = Game(6, players, events)
    game.pass_hand()

    card_nums: list[int] = []

    # Constructs a list of the card numbers of their (new) hand
    for _, card in players[player].child_hand.items():
        card_nums.append(card["number"])

    assert card_nums == out_hand


@pytest.mark.parametrize(
    "player_num",
    [
        (1),
        (2),
        (3),
        (4),
        (5),
        (6),
    ],
)
def test_event_phase(player_num):
    players = create_players(6, test_deals)
    events = deal_events()
    game = Game(6, players, events)

    for _, player in players.items():
        for attribute in [
            "Constitution",
            "Coordination",
            "Creativity",
            "Determination",
            "Empathy",
            "Intelligence",
            "Sociability",
            "Strength",
        ]:
            setattr(player.board, attribute, 20)

    game.event_phase()

    assert players[player_num].points != 0


@pytest.mark.parametrize("function", [("card_phase"), ("pass_hand"), ("event_phase")])
def test_play_turn(function) -> None:
    """Tests that the play turn method calls the correct functions. Mocks the function calls
    and validates that each one is called"""
    players = create_players(6, test_deals)
    events = deal_events()
    game = Game(6, players, events)
    # Create a mock version of the function, which can then be checked to see if it was called
    setattr(game, function, MagicMock())
    game.play_turn(1)
    assert getattr(game, function).called


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_play_round(round) -> None:
    """Tests that the play_round method correctly calls the play_turn method 4 times"""
    players = create_players(6, test_deals)
    events = deal_events()
    game = Game(6, players, events)
    game.curr_round = round
    game.play_turn = MagicMock()
    game.play_round()
    assert game.play_turn.call_count == 4


def test_game_play_game() -> None:
    """Tests that the play_game method correctly calls the play_round method 3 times"""
    players = create_players(6, test_deals)
    events = deal_events()
    game = Game(6, players, events)
    game.play_round = MagicMock()
    game.play_game()
    assert game.play_round.call_count == 3
