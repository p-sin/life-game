import pytest
import copy

from life_game.setup.components import attribute_slots
from life_game.play.players import create_players
from life_game.setup.cards import cards

test_deals = {
    "child": [1, 5, 23, 27, 34, 35, 43, 48, 51],
    "adol": [63, 76, 79, 85, 89, 101, 111, 115, 120],
    "adult": [125, 132, 138, 144, 148, 153, 156, 167, 179],
}


def test_player_choose_cards_is_card() -> None:
    """Tests that the outputs are card objects"""
    deals = test_deals
    players = create_players(1, deals)

    chosen_cards = players[1].choose_cards("child", 1)

    try:
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

    chosen_cards = players[1].choose_cards(round, 1)

    for card in chosen_cards:
        assert card["number"] in card_range


def test_player_choose_cards_unique() -> None:
    """Test that the cards chosen are not the same"""
    deals = test_deals
    players = create_players(1, deals)

    unique = True

    for _ in range(200):
        chosen_cards = players[1].choose_cards("child", 1)
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
    deals = test_deals
    players = create_players(1, deals)

    for _ in range(100):
        chosen_cards = players[1].choose_cards("child", turn)

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
    """Test that the chosen cards are correctly applied to the player board"""
    players = create_players(1, test_deals)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[1].play_cards(chosen_cards)

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
    """Test that the chosen cards are correctly applied to the player board"""
    players = create_players(player, test_deals)

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
    "player, round, hand, card_1, card_2, outcome",
    [
        (1, "child", "child_hand", 0, 1, [23, 27, 34, 35, 43, 48, 51]),
        (1, "adol", "adol_hand", 2, 3, [63, 76, 89, 101, 111, 115, 120]),
        (1, "adult", "adult_hand", 4, 5, [125, 132, 138, 144, 156, 167, 179]),
        (2, "child", "child_hand", 17, 16, [2, 6, 24, 28, 36, 37, 44]),
        (2, "adol", "adol_hand", 15, 14, [62, 75, 78, 84, 88, 114, 119]),
        (2, "adult", "adult_hand", 13, 12, [126, 133, 139, 154, 157, 168, 180]),
    ],
)
def test_remove_cards_removed(player, round, hand, card_1, card_2, outcome) -> None:
    players = create_players(2, test_deals_2)
    chosen_cards = [
        cards[test_deals_2[round][card_1]],
        cards[test_deals_2[round][card_2]],
    ]

    players[player].remove_cards(chosen_cards, round)

    hand = getattr(players[player], hand)

    card_list = []

    for num, card in hand.items():
        card_list.append(card["number"])

    assert card_list == outcome


@pytest.mark.parametrize(
    "card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8",
    [
        (0, 1, 2, 3, 4, 5, 6, 7),
        (8, 2, 5, 4, 1, 6, 7, 0),
        (8, 2, 4, 1, 6, 3, 7, 0),
        (4, 2, 5, 3, 1, 6, 7, 0),
        (8, 2, 5, 4, 1, 6, 3, 7),
    ],
)
def test_remove_cards_deplete(
    card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8
) -> None:
    players = create_players(2, test_deals_2)

    card_list = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8]

    for x, y in zip([0, 2, 4, 6], [1, 3, 5, 7]):
        chosen_cards = [
            cards[test_deals_2["child"][card_list[x]]],
            cards[test_deals_2["child"][card_list[y]]],
        ]
        players[1].remove_cards(chosen_cards, "child")

    assert list(players[1].child_hand.keys()) == [1]


def test_remove_cards_position() -> None:
    players = create_players(2, test_deals_2)
    chosen_cards = [
        cards[test_deals_2["child"][10]],
        cards[test_deals_2["child"][13]],
    ]
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
    players = create_players(player, test_deals)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[card_3], cards[card_4]]
    players[player].play_cards(chosen_cards)
    chosen_cards = [cards[card_5], cards[card_6]]
    players[player].play_cards(chosen_cards)
    players[player].calculate_attribute_totals()

    assert getattr(players[player].board, attribute) == value
