import pytest
import copy

from life_game.setup.components import attribute_slots
from life_game.play.players import create_players
from life_game.setup.attr_cards import cards

# Sample deal used for several tests to fix the input
test_deals = {
    "child": [1, 5, 23, 27, 34, 35, 43, 48, 51],
    "adol": [63, 76, 79, 85, 89, 101, 111, 115, 120],
    "adult": [125, 132, 138, 144, 148, 153, 156, 167, 179],
}


def test_player_choose_cards_is_card() -> None:
    """Tests that the outputs are card objects by checking they are a dict with a "slot_number" key"""
    deals = test_deals
    players = create_players(1, deals)

    # Choose cards from the fixed deal
    chosen_cards, _ = players[1].choose_cards("child", 1)

    try:
        # The card has a 'slot_number'
        chosen_cards[0]["card_slot_1"]["slot_number"]
        assert True
    except:
        assert False


@pytest.mark.parametrize(
    "round, card_range",
    [
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
    ],
)
def test_player_choose_cards_exist(round, card_range) -> None:
    """Test that the card objects chosen exist in the deal supplied to the function"""
    deals = test_deals
    players = create_players(1, deals)

    chosen_cards, _ = players[1].choose_cards(round, 1)

    # Chosen card is one of the cards given in the fixed deal
    for card in chosen_cards:
        assert card["number"] in card_range


def test_player_choose_cards_unique() -> None:
    """Test that the cards chosen are not the same"""
    deals = test_deals
    players = create_players(1, deals)

    unique = True

    for _ in range(200):
        # It never chooses the same card
        chosen_cards, _ = players[1].choose_cards("child", 1)
        if chosen_cards[0]["number"] == chosen_cards[1]["number"]:
            unique = False

    assert unique == True


@pytest.mark.parametrize(
    "turn, cards_in_scope",
    [
        (1, [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        (2, [1, 5, 23, 27, 34, 35, 43]),
        (3, [1, 5, 23, 27, 34]),
        (4, [1, 5, 23]),
    ],
)
def test_player_choose_cards_turn(turn, cards_in_scope) -> None:
    """Test that the chosen card is one of the 'in scope' cards, which simulates the
    removal of cards over 4 turns"""
    deals = test_deals
    players = create_players(1, deals)

    # Uses the turn value to reduce the range of cards it can choose from (e.g 9/7/5/3)
    for _ in range(100):
        chosen_cards, _ = players[1].choose_cards("child", turn)

        # It chose a card from the specified range of available cards
        for card in chosen_cards:
            assert card["number"] in cards_in_scope


@pytest.mark.parametrize(
    "card_1, card_2, slot_1, type_1, value_1, slot_2, type_2, value_2, slot_3, type_3, value_3",
    [
        (
            1,
            36,
            "attr_slot_1",
            "Sociability",
            2,
            "attr_slot_2",
            "Sociability",
            1,
            "attr_slot_3",
            "Creativity",
            1,
        ),
        (
            71,
            75,
            "attr_slot_12",
            "Constitution",
            3,
            "attr_slot_13",
            "Coordination",
            3,
            "attr_slot_14",
            "",
            0,
        ),
        (
            179,
            180,
            "attr_slot_23",
            "Empathy",
            2,
            "attr_slot_24",
            "Determination",
            2,
            "attr_slot_22",
            "",
            0,
        ),
    ],
)
def test_player_play_card(
    card_1,
    card_2,
    slot_1,
    type_1,
    value_1,
    slot_2,
    type_2,
    value_2,
    slot_3,
    type_3,
    value_3,
) -> None:
    """Test that the chosen cards are correctly applied to the player board over a single turn"""
    players = create_players(1, test_deals)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[1].play_cards(chosen_cards)

    # Two cards played each time. Updates a test version of board below and compares to actual board
    test_attribute_slots = copy.deepcopy(attribute_slots)
    test_attribute_slots[slot_1]["type"] = type_1
    test_attribute_slots[slot_1]["value"] = value_1
    test_attribute_slots[slot_2]["type"] = type_2
    test_attribute_slots[slot_2]["value"] = value_2
    test_attribute_slots[slot_3]["type"] = type_3
    test_attribute_slots[slot_3]["value"] = value_3

    assert players[1].board.attribute_slots == test_attribute_slots


@pytest.mark.parametrize(
    "player",
    [
        (1),
        (2),
        (3),
        (4),
        (5),
        (6),
    ],
)
def test_player_play_card_multiple_plays(player) -> None:
    """Test that the chosen cards are correctly applied to the player board over multiple turns"""
    players = create_players(player, test_deals)

    # Same as before, but plays several cards in sequence
    chosen_cards = [cards[1], cards[2]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[7], cards[13]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[14], cards[1]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[23], cards[29]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[35], cards[2]]
    players[player].play_cards(chosen_cards)

    test_attribute_slots_2 = copy.deepcopy(attribute_slots)
    test_attribute_slots_2["attr_slot_1"]["type"] = "Intelligence"
    test_attribute_slots_2["attr_slot_1"]["value"] = 2
    test_attribute_slots_2["attr_slot_2"]["type"] = "Sociability"
    test_attribute_slots_2["attr_slot_2"]["value"] = 1
    test_attribute_slots_2["attr_slot_3"]["type"] = "Intelligence"
    test_attribute_slots_2["attr_slot_3"]["value"] = 1
    test_attribute_slots_2["attr_slot_5"]["type"] = "Constitution"
    test_attribute_slots_2["attr_slot_5"]["value"] = 2

    assert players[player].board.attribute_slots == test_attribute_slots_2


test_deals_2 = {
    "child": [1, 5, 23, 27, 34, 35, 43, 48, 51, 2, 6, 24, 28, 36, 37, 44, 49, 52],
    "adol": [
        63,
        76,
        79,
        85,
        89,
        101,
        111,
        115,
        120,
        62,
        75,
        78,
        84,
        88,
        100,
        110,
        114,
        119,
    ],
    "adult": [
        125,
        132,
        138,
        144,
        148,
        153,
        156,
        167,
        179,
        126,
        133,
        139,
        145,
        149,
        154,
        157,
        168,
        180,
    ],
}


@pytest.mark.parametrize(
    "player, round, hand, card_order, outcome_1, outcome_2, outcome_3, outcome_4",
    [
        (
            1,
            "child",
            "child_hand",
            [6, 7, 2, 7, 1, 2, 2, 3],
            [1, 5, 23, 27, 34, 48, 51],
            [1, 23, 27, 34, 48],
            [27, 34, 48],
            [27],
        ),
        (
            1,
            "adol",
            "adol_hand",
            [1, 2, 1, 2, 1, 2, 1, 2],
            [79, 85, 89, 101, 111, 115, 120],
            [89, 101, 111, 115, 120],
            [111, 115, 120],
            [120],
        ),
        (
            2,
            "adol",
            "adol_hand",
            [8, 9, 6, 7, 4, 5, 2, 3],
            [62, 75, 78, 84, 88, 100, 110],
            [62, 75, 78, 84, 88],
            [62, 75, 78],
            [62],
        ),
        (
            2,
            "adult",
            "adult_hand",
            [5, 4, 5, 4, 5, 4, 3, 1],
            [126, 133, 139, 154, 157, 168, 180],
            [126, 133, 139, 168, 180],
            [126, 133, 139],
            [133],
        ),
    ],
)
def test_remove_cards_removed(
    player, round, hand, card_order, outcome_1, outcome_2, outcome_3, outcome_4
) -> None:
    """Tests that the correct cards are removed from the player's hand across several turns"""
    players = create_players(2, test_deals_2)

    # Simulates turns by having it select different values from the 'card_order'. Each loop
    # is a new turn and it changes the definition of card_1 and card_2 - functionally just
    # shifts along the card_order list to simulate 2 new cards being chosen each turn.
    # Each turn has a different outcome as the remaining cards reduce. The 4 outcomes
    # match the 4 turns
    for card_1, card_2, outcome in zip(
        [0, 2, 4, 6], [1, 3, 5, 7], [outcome_1, outcome_2, outcome_3, outcome_4]
    ):
        # Choose the two cards for this turn
        chosen_cards = [
            card_order[card_1],
            card_order[card_2],
        ]

        players[player].remove_cards(chosen_cards, round)

        # Get the new hand generated from removing the cards
        hand_contents = getattr(players[player], hand)

        card_list = []

        # Get all the card numbers from the hand and check against the expected outcome for this turn
        for _, card in hand_contents.items():
            card_list.append(card["number"])

        assert card_list == outcome


@pytest.mark.parametrize(
    "card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8",
    [
        (8, 7, 6, 5, 4, 3, 2, 1),
        (8, 2, 5, 4, 1, 3, 1, 2),
        (8, 2, 4, 1, 5, 3, 2, 3),
        (4, 2, 5, 3, 1, 3, 1, 3),
        (8, 2, 5, 4, 1, 4, 3, 1),
    ],
)
def test_remove_cards_deplete(
    card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8
) -> None:
    """Tests that the player's hand is correctly depleted by removing hands"""
    players = create_players(2, test_deals_2)

    card_list = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8]

    # Remove cards over 4 'turns'
    for x, y in zip([0, 2, 4, 6], [1, 3, 5, 7]):
        chosen_cards_pos = [
            card_list[x],
            card_list[y],
        ]
        players[1].remove_cards(chosen_cards_pos, "child")

    # Only one card left
    assert list(players[1].child_hand.keys()) == [1]


def test_remove_cards_position() -> None:
    """Tests that the new hand is correctly indexed with consecutive numbers"""
    players = create_players(2, test_deals_2)
    chosen_cards = [7, 3]
    players[2].remove_cards(chosen_cards, "child")

    assert list(players[2].child_hand.keys()) == [1, 2, 3, 4, 5, 6, 7]


@pytest.mark.parametrize(
    "player, card_1, card_2, card_3, card_4, card_5, card_6, attribute, value",
    [
        (1, 1, 4, 45, 89, 103, 167, "Sociability", 6),
        (1, 1, 4, 45, 89, 103, 167, "Intelligence", 2),
        (1, 1, 4, 45, 89, 103, 167, "Creativity", 0),
        (1, 1, 4, 45, 89, 103, 167, "Strength", 5),
        (1, 1, 4, 45, 89, 103, 167, "Constitution", 4),
        (1, 1, 4, 45, 89, 103, 167, "Coordination", 1),
        (1, 1, 4, 45, 89, 103, 167, "Empathy", 0),
        (1, 1, 4, 45, 89, 103, 167, "Determination", 0),
        (2, 10, 24, 65, 154, 156, 179, "Sociability", 3),
        (2, 10, 24, 65, 154, 156, 179, "Intelligence", 3),
        (2, 10, 24, 65, 154, 156, 179, "Creativity", 5),
        (2, 10, 24, 65, 154, 156, 179, "Strength", 2),
        (2, 10, 24, 65, 154, 156, 179, "Constitution", 0),
        (2, 10, 24, 65, 154, 156, 179, "Coordination", 0),
        (2, 10, 24, 65, 154, 156, 179, "Empathy", 2),
        (2, 10, 24, 65, 154, 156, 179, "Determination", 2),
        (3, 34, 76, 99, 101, 104, 154, "Sociability", 2),
        (3, 34, 76, 99, 101, 104, 154, "Intelligence", 3),
        (3, 34, 76, 99, 101, 104, 154, "Creativity", 5),
        (3, 34, 76, 99, 101, 104, 154, "Strength", 3),
        (3, 34, 76, 99, 101, 104, 154, "Constitution", 2),
        (3, 34, 76, 99, 101, 104, 154, "Coordination", 2),
        (3, 34, 76, 99, 101, 104, 154, "Empathy", 0),
        (3, 34, 76, 99, 101, 104, 154, "Determination", 0),
        (4, 55, 66, 77, 88, 99, 110, "Sociability", 2),
        (4, 55, 66, 77, 88, 99, 110, "Intelligence", 0),
        (4, 55, 66, 77, 88, 99, 110, "Creativity", 4),
        (4, 55, 66, 77, 88, 99, 110, "Strength", 1),
        (4, 55, 66, 77, 88, 99, 110, "Constitution", 3),
        (4, 55, 66, 77, 88, 99, 110, "Coordination", 2),
        (4, 55, 66, 77, 88, 99, 110, "Empathy", 0),
        (4, 55, 66, 77, 88, 99, 110, "Determination", 0),
        (5, 23, 83, 112, 144, 161, 169, "Sociability", 5),
        (5, 23, 83, 112, 144, 161, 169, "Intelligence", 3),
        (5, 23, 83, 112, 144, 161, 169, "Creativity", 2),
        (5, 23, 83, 112, 144, 161, 169, "Strength", 2),
        (5, 23, 83, 112, 144, 161, 169, "Constitution", 6),
        (5, 23, 83, 112, 144, 161, 169, "Coordination", 2),
        (5, 23, 83, 112, 144, 161, 169, "Empathy", 0),
        (5, 23, 83, 112, 144, 161, 169, "Determination", 0),
        (6, 5, 15, 35, 95, 105, 155, "Sociability", 5),
        (6, 5, 15, 35, 95, 105, 155, "Intelligence", 5),
        (6, 5, 15, 35, 95, 105, 155, "Creativity", 0),
        (6, 5, 15, 35, 95, 105, 155, "Strength", 2),
        (6, 5, 15, 35, 95, 105, 155, "Constitution", 0),
        (6, 5, 15, 35, 95, 105, 155, "Coordination", 4),
        (6, 5, 15, 35, 95, 105, 155, "Empathy", 0),
        (6, 5, 15, 35, 95, 105, 155, "Determination", 0),
    ],
)
def test_player_calc_attributes(
    player, card_1, card_2, card_3, card_4, card_5, card_6, attribute, value
) -> None:
    """Tests that each player's attribute totals are correctly updated after playing several cards"""
    # The test repeats the same process for each player and attribute, but only tests one attribute
    # on each iteration
    players = create_players(player, test_deals)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[card_3], cards[card_4]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[card_5], cards[card_6]]
    players[player].play_cards(chosen_cards)
    players[player].calculate_attribute_totals()

    assert getattr(players[player].board, attribute) == value
