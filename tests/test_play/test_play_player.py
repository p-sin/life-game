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

    chosen_cards = players[1].choose_cards("child")

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

    chosen_cards = players[1].choose_cards(round)

    for card in chosen_cards:
        assert card["number"] in card_range


def test_player_choose_cards_unique() -> None:
    """Test that the cards chosen are not the same"""
    deals = test_deals
    players = create_players(1, deals)

    unique = True

    for _ in range(200):
        chosen_cards = players[1].choose_cards("child")
        if chosen_cards[0]["number"] == chosen_cards[1]["number"]:
            unique = False

    assert unique == True


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


@pytest.mark.parametrize(
    "player, card_1, card_2, card_3, card_4, card_5, card_6, 
    Sociability, Intelligence, Creativity, Strength, Constitution, Coordination, Empathy, Determination",
    [
        (1, 1, 4, 45, 89, 103, 167, 5, 2, 0, 5, 4, 1, 0, 0),
        (2, 10, 24, 65, 154, 156, 179, 3, 3, 5, 2, 0, 0, 2, 2),
        (3, 34, 76, 99, 101, 104, 154, 2, 3, 5, 3, 2, 2, 0, 0),
        (4, 55, 66, 77, 88, 99, 110, 2, 4, 3, 1, 6, 2, 0, 0),
        (5, 23, 83, 112, 144, 161, 169, 5, 3, 2, 4, 4, 2, 0, 0),
        (6, 5, 15, 35, 95, 105, 155, 0, 0, 0, 0, 0, 0, 0, 0),
    ],
)
def test_player_calc_attributes() -> None:
    players = create_players(1, test_deals)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[1].play_cards(chosen_cards)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[1].play_cards(chosen_cards)
    chosen_cards = [cards[card_1], cards[card_2]]
    players[1].play_cards(chosen_cards)
    players[1].calculate_attribute_totals()
