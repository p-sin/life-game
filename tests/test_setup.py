import pytest
from life_game.setup.definitions import Attributes, BoardSlots
from life_game.setup.cards import cards

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
    try:
        assert Attributes[enum].value.name == name and Attributes[enum].value.value == value
    except:
        assert False 
       
@pytest.mark.parametrize(
    "enum, number, body, stage, slot_1, slot_2, slot_3",
    [
    ("BOARD_SLOT_ONE", 1, "mind", "child", 1, 2, 3),
    ("BOARD_SLOT_TWO", 2, "body", "child", 4, 5, 6),
    ("BOARD_SLOT_THREE", 3, "soul", "child", 7, 8, None),
    ("BOARD_SLOT_FOUR", 4, "mind", "adolescent", 9, 10, 11),
    ("BOARD_SLOT_FIVE", 5, "body", "adolescent", 12, 13, 14),
    ("BOARD_SLOT_SIX", 6, "soul", "adolescent", 15, 16, None),
    ("BOARD_SLOT_SEVEN", 7, "mind", "adult", 17, 18, 19),
    ("BOARD_SLOT_EIGHT", 8, "body", "adult", 20, 21, 22),
    ("BOARD_SLOT_NINE", 9, "soul", "adult", 23, 24, None),
    ]
)

def test_body_slot_enum_defined(enum, number, body, stage, slot_1, slot_2, slot_3):
    try:
        assert BoardSlots[enum].value.number == number and BoardSlots[enum].value.body_part == body and BoardSlots[enum].value.life_stage == stage and BoardSlots[enum].value.card_slot_1 == slot_1 and BoardSlots[enum].value.card_slot_2 == slot_2 and BoardSlots[enum].value.card_slot_3 == slot_3
    except Exception as e:
        print (e)
        assert False 


def test_number_cards():
    assert len(cards) == 60

    
def test_cards_by_board_slot():

    expected_dict = {
        1: 27,
        2: 27,
        3: 6,
    }

    actual_dict = {}

    for key, dict in cards.items():
        if dict["board_slot"].value.number not in actual_dict.keys():
            actual_dict[dict["board_slot"].value.number] = 0
        actual_dict[dict["board_slot"].value.number] += 1

    assert actual_dict == expected_dict

