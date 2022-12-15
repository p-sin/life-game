import pytest
from life_game.setup.components import Attributes, BoardSections, decks
from life_game.setup.cards import cards
from life_game.setup.players import setup_players, deal_cards, Player

@pytest.mark.parametrize(
    "enum, name, value",
    [
    ("SOCIAL_ONE", "Sociability", 1),
    ("SOCIAL_TWO", "Sociability", 2),
    ("SOCIAL_THREE", "Sociability", 3),
    ("SOCIAL_FOUR", "Sociability", 4),
    ("INTEL_ONE", "Intelligence", 1),
    ("INTEL_TWO", "Intelligence", 2),
    ("INTEL_THREE", "Intelligence", 3),
    ("INTEL_FOUR", "Intelligence", 4),
    ("CREATE_ONE", "Creativity", 1),
    ("CREATE_TWO", "Creativity", 2),
    ("CREATE_THREE", "Creativity", 3),
    ("CREATE_FOUR", "Creativity", 4),
    ("STRENGTH_ONE", "Strength", 1),
    ("STRENGTH_TWO", "Strength", 2),
    ("STRENGTH_THREE", "Strength", 3),
    ("STRENGTH_FOUR", "Strength", 4),
    ("CONST_ONE", "Constitution", 1),
    ("CONST_TWO", "Constitution", 2),
    ("CONST_THREE", "Constitution", 3),
    ("CONST_FOUR", "Constitution", 4),
    ("COORD_ONE", "Co-ordination", 1),
    ("COORD_TWO", "Co-ordination", 2),
    ("COORD_THREE", "Co-ordination", 3),
    ("COORD_FOUR", "Co-ordination", 4),
    ("EMPATHY_ONE", "Empathy", 1),
    ("EMPATHY_TWO", "Empathy", 2),
    ("EMPATHY_THREE", "Empathy", 3),
    ("EMPATHY_FOUR", "Empathy", 4),
    ("DETERM_ONE", "Determination", 1),
    ("DETERM_TWO", "Determination", 2),
    ("DETERM_THREE", "Determination", 3),
    ("DETERM_FOUR", "Determination", 4),
    ]
)

def test_attribute_enum_defined(enum, name, value):
    """Test that the Attributes Enum is correct"""
    try:
        assert Attributes[enum].value.name == name and Attributes[enum].value.value == value
    except:
        assert False 
       
@pytest.mark.parametrize(
    "enum, number, body, stage, slot_1, slot_2, slot_3",
    [
    ("BOARD_SECTION_ONE", 1, "mind", "child", "attr_slot_1", "attr_slot_2", "attr_slot_3"),
    ("BOARD_SECTION_TWO", 2, "body", "child", "attr_slot_4", "attr_slot_5", "attr_slot_6"),
    ("BOARD_SECTION_THREE", 3, "soul", "child", "attr_slot_7", "attr_slot_8", None),
    ("BOARD_SECTION_FOUR", 4, "mind", "adolescent", "attr_slot_9", "attr_slot_10", "attr_slot_11"),
    ("BOARD_SECTION_FIVE", 5, "body", "adolescent", "attr_slot_12", "attr_slot_13", "attr_slot_14"),
    ("BOARD_SECTION_SIX", 6, "soul", "adolescent", "attr_slot_15", "attr_slot_16", None),
    ("BOARD_SECTION_SEVEN", 7, "mind", "adult", "attr_slot_17", "attr_slot_18", "attr_slot_19"),
    ("BOARD_SECTION_EIGHT", 8, "body", "adult", "attr_slot_20", "attr_slot_21", "attr_slot_22"),
    ("BOARD_SECTION_NINE", 9, "soul", "adult", "attr_slot_23", "attr_slot_24", None),
    ]
)

def test_body_slot_enum_defined(enum, number, body, stage, slot_1, slot_2, slot_3):
    """Test that the BoardSection enum is correct"""
    try:
        assert BoardSections[enum].value.number == number and BoardSections[enum].value.body_part == body and BoardSections[enum].value.life_stage == stage and BoardSections[enum].value.card_slot_1 == slot_1 and BoardSections[enum].value.card_slot_2 == slot_2 and BoardSections[enum].value.card_slot_3 == slot_3
    except Exception as e:
        print (e)
        assert False 


def test_card_number():
    """Test the correct number of cards have been defined"""
    assert len(cards) == 180

    
def test_board_section_number():
    """Test that the cards have the correct attributes"""

    expected_dict = {
        1: 27,
        2: 27,
        3: 6,
        4: 27,
        5: 27,
        6: 6,
        7: 27,
        8: 27,
        9: 6,
    }

    actual_dict = {}

    for _, dict in cards.items():
        if dict["board_section"].value.number not in actual_dict.keys():
            actual_dict[dict["board_section"].value.number] = 0
        actual_dict[dict["board_section"].value.number] += 1

    assert actual_dict == expected_dict

@pytest.mark.parametrize(
    "card_slot, values",
    [
        ("card_slot_1", ["attr_slot_1", "attr_slot_4", "attr_slot_7", "attr_slot_9", "attr_slot_12", "attr_slot_15", "attr_slot_17", "attr_slot_20", "attr_slot_23"]),
        ("card_slot_2", ["attr_slot_2", "attr_slot_5", "attr_slot_8", "attr_slot_10", "attr_slot_13", "attr_slot_16", "attr_slot_18", "attr_slot_21", "attr_slot_24"]),
        ("card_slot_3", ["attr_slot_3", "attr_slot_6", "attr_slot_11", "attr_slot_14", "attr_slot_19", "attr_slot_22"])
    ]
)
def test_card_slot_valid(card_slot: str, values: list[str]) -> None:
    """Test each card slot has a valid attribute slot assigned to it"""

    for _, dict in cards.items():
        if dict[card_slot]["slot_number"] is None:
            assert True
        else:
            assert dict[card_slot]["slot_number"] in values


@pytest.mark.parametrize(
    "card_slot",
    [
        ("card_slot_1"),
        ("card_slot_2"),
        ("card_slot_3")
    ]
)
def test_board_section_match(card_slot: str) -> None:

    for _, dict in cards.items():
        if dict[card_slot]["slot_number"] is None:
            assert True
        else:
            assert getattr(dict["board_section"].value, card_slot) == dict[card_slot]["slot_number"]


def test_cards_by_attribute():
    expected_dict = {
        "Sociability": 87,
        "Intelligence": 87,
        "Creativity": 87,
        "Strength": 87,
        "Constitution": 87,
        "Co-ordination": 87,
        "Empathy": 28,
        "Determination": 28,

    }

    actual_dict = {}

    for _, dict in cards.items():

        if dict["card_slot_1"]["values"] is not None:

            if dict["card_slot_1"]["values"].value.name not in actual_dict.keys():
                actual_dict[dict["card_slot_1"]["values"].value.name] = 0
            actual_dict[dict["card_slot_1"]["values"].value.name] += dict["card_slot_1"]["values"].value.value

        if dict["card_slot_2"]["values"] is not None:
            if dict["card_slot_2"]["values"].value.name not in actual_dict.keys():
                actual_dict[dict["card_slot_2"]["values"].value.name] = 0
            actual_dict[dict["card_slot_2"]["values"].value.name] += dict["card_slot_2"]["values"].value.value
        
        if dict["card_slot_3"]["values"] is not None:
            if dict["card_slot_3"]["values"].value.name not in actual_dict.keys():
                actual_dict[dict["card_slot_3"]["values"].value.name] = 0
            actual_dict[dict["card_slot_3"]["values"].value.name] += dict["card_slot_3"]["values"].value.value

    assert actual_dict == expected_dict


def test_deck_by_attribute():
    expected_dict = {
        "Sociability": 87,
        "Intelligence": 87,
        "Creativity": 87,
        "Strength": 87,
        "Constitution": 87,
        "Co-ordination": 87,
        "Empathy": 126,
        "Determination": 126,

    }

    actual_dict = {}
    deck = decks["child"] + decks["adol"] + decks["adult"]

    for card_num in deck:
        card = cards[card_num]

        if card["card_slot_1"]["values"] is not None:

            if card["card_slot_1"]["values"].value.name not in actual_dict.keys():
                actual_dict[card["card_slot_1"]["values"].value.name] = 0
            actual_dict[card["card_slot_1"]["values"].value.name] += card["card_slot_1"]["values"].value.value

        if card["card_slot_2"]["values"] is not None:
            if card["card_slot_2"]["values"].value.name not in actual_dict.keys():
                actual_dict[card["card_slot_2"]["values"].value.name] = 0
            actual_dict[card["card_slot_2"]["values"].value.name] += card["card_slot_2"]["values"].value.value
        
        if card["card_slot_3"]["values"] is not None:
            if card["card_slot_3"]["values"].value.name not in actual_dict.keys():
                actual_dict[card["card_slot_3"]["values"].value.name] = 0
            actual_dict[card["card_slot_3"]["values"].value.name] += card["card_slot_3"]["values"].value.value

    assert actual_dict == expected_dict

def test_setup_player_count() -> None:
    player_info, num_players = setup_players(3)

    assert num_players == [1,2,3]

def test_setup_player_info_count() -> None:

    player_info, num_players = setup_players(2)

    assert list(player_info.keys()) == [1,2]

def test_setup_player_info_type() -> None:

    player_info, num_players = setup_players(1)

    assert isinstance(player_info[1], Player)

