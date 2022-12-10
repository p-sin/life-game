from enum import Enum
from dataclasses import dataclass
from typing import Optional

@dataclass
class AttributeInfo:
    name: str
    value: int

class Attributes(Enum):
    SOCIAL_ONE = AttributeInfo(
        name = "Sociability",
        value = 1,
    )
    SOCIAL_TWO = AttributeInfo(
        name = "Sociability",
        value = 2,
    )
    SOCIAL_THREE = AttributeInfo(
        name = "Sociability",
        value = 3,
    )
    SOCIAL_FOUR = AttributeInfo(
        name = "Sociability",
        value = 4,
    )
    INTEL_ONE = AttributeInfo(
        name = "Intelligence",
        value = 1,
    )
    INTEL_TWO = AttributeInfo(
        name = "Intelligence",
        value = 2,
    )
    INTEL_THREE = AttributeInfo(
        name = "Intelligence",
        value = 3,
    )
    INTEL_FOUR = AttributeInfo(
        name = "Intelligence",
        value = 4,
    )
    CREATE_ONE = AttributeInfo(
        name = "Creativity",
        value = 1,
    )
    CREATE_TWO = AttributeInfo(
        name = "Creativity",
        value = 2,
    )
    CREATE_THREE = AttributeInfo(
        name = "Creativity",
        value = 3,
    )
    CREATE_FOUR = AttributeInfo(
        name = "Creativity",
        value = 4,
    )
    STRENGTH_ONE = AttributeInfo(
        name = "Strength",
        value = 1,
    )
    STRENGTH_TWO = AttributeInfo(
        name = "Strength",
        value = 2,
    )
    STRENGTH_THREE = AttributeInfo(
        name = "Strength",
        value = 3,
    )
    STRENGTH_FOUR = AttributeInfo(
        name = "Strength",
        value = 4,
    )
    CONST_ONE = AttributeInfo(
        name = "Constitution",
        value = 1,
    )
    CONST_TWO = AttributeInfo(
        name = "Constitution",
        value = 2,
    )
    CONST_THREE = AttributeInfo(
        name = "Constitution",
        value = 3,
    )
    CONST_FOUR = AttributeInfo(
        name = "Constitution",
        value = 4,
    )
    COORD_ONE = AttributeInfo(
        name = "Co-ordination",
        value = 1,
    )
    COORD_TWO = AttributeInfo(
        name = "Co-ordination",
        value = 2,
    )
    COORD_THREE = AttributeInfo(
        name = "Co-ordination",
        value = 3,
    )
    COORD_FOUR = AttributeInfo(
        name = "Co-ordination",
        value = 4,
    )
    EMPATHY_ONE = AttributeInfo(
        name = "Empathy",
        value = 1,
    )
    EMPATHY_TWO = AttributeInfo(
        name = "Empathy",
        value = 2,
    )
    EMPATHY_THREE = AttributeInfo(
        name = "Empathy",
        value = 3,
    )
    EMPATHY_FOUR = AttributeInfo(
        name = "Empathy",
        value = 4,
    )
    DETERM_ONE = AttributeInfo(
        name = "Determination",
        value = 1,
    )
    DETERM_TWO = AttributeInfo(
        name = "Determination",
        value = 2,
    )
    DETERM_THREE = AttributeInfo(
        name = "Determination",
        value = 3,
    )
    DETERM_FOUR = AttributeInfo(
        name = "Determination",
        value = 4,
    )

@dataclass
class BoardSectionInfo:
    number: int
    body_part: str
    life_stage: str
    card_slot_1: int
    card_slot_2: int
    card_slot_3: Optional[int]

class BoardSections(Enum):
    BOARD_SECTION_ONE = BoardSectionInfo(
        number = 1,
        body_part = "mind",
        life_stage = "child",
        card_slot_1 = 1,
        card_slot_2 = 2,
        card_slot_3 = 3,
    )
    BOARD_SECTION_TWO = BoardSectionInfo(
        number = 2,
        body_part = "body",
        life_stage = "child",
        card_slot_1 = 4,
        card_slot_2 = 5,
        card_slot_3 = 6,
    )
    BOARD_SECTION_THREE = BoardSectionInfo(
        number = 3,
        body_part = "soul",
        life_stage = "child",
        card_slot_1 = 7,
        card_slot_2 = 8,
        card_slot_3 = None,
    )
    BOARD_SECTION_FOUR = BoardSectionInfo(
        number = 4,
        body_part = "mind",
        life_stage = "adolescent",
        card_slot_1 = 9,
        card_slot_2 = 10,
        card_slot_3 = 11,
    )
    BOARD_SECTION_FIVE = BoardSectionInfo(
        number = 5,
        body_part = "body",
        life_stage = "adolescent",
        card_slot_1 = 12,
        card_slot_2 = 13,
        card_slot_3 = 14,
    )
    BOARD_SECTION_SIX = BoardSectionInfo(
        number = 6,
        body_part = "soul",
        life_stage = "adolescent",
        card_slot_1 = 15,
        card_slot_2 = 16,
        card_slot_3 = None,
    )
    BOARD_SECTION_SEVEN = BoardSectionInfo(
        number = 7,
        body_part = "mind",
        life_stage = "adult",
        card_slot_1 = 17,
        card_slot_2 = 18,
        card_slot_3 = 19,
    )
    BOARD_SECTION_EIGHT = BoardSectionInfo(
        number = 8,
        body_part = "body",
        life_stage = "adult",
        card_slot_1 = 20,
        card_slot_2 = 21,
        card_slot_3 = 22,
    )
    BOARD_SECTION_NINE = BoardSectionInfo(
        number = 9,
        body_part = "soul",
        life_stage = "adult",
        card_slot_1 = 23,
        card_slot_2 = 24,
        card_slot_3 = None,
    )

@dataclass
class Board:
    """Defines the playerboard"""
    player: int
    sociability: int
    intelligence: int
    creativity: int	
    strength: int
    constitution: int
    coordination: int
    empathy: int
    determination: int
    atrr_slot_1: str
    atrr_slot_2: str
    atrr_slot_3: str
    atrr_slot_4: str
    atrr_slot_5: str
    atrr_slot_6: str
    atrr_slot_7: str
    atrr_slot_8: str
    atrr_slot_9: str
    atrr_slot_10: str
    atrr_slot_11: str
    atrr_slot_12: str
    atrr_slot_13: str
    atrr_slot_14: str
    atrr_slot_15: str
    atrr_slot_16: str
    atrr_slot_17: str
    atrr_slot_18: str
    atrr_slot_19: str
    atrr_slot_20: str
    atrr_slot_21: str
    atrr_slot_22: str
    atrr_slot_23: str
    atrr_slot_24: str
    value_slot_1: int
    value_slot_2: int
    value_slot_3: int
    value_slot_4: int
    value_slot_5: int
    value_slot_6: int
    value_slot_7: int
    value_slot_8: int
    value_slot_9: int
    value_slot_10: int
    value_slot_11: int
    value_slot_12: int
    value_slot_13: int
    value_slot_14: int
    value_slot_15: int
    value_slot_16: int
    value_slot_17: int
    value_slot_18: int
    value_slot_19: int
    value_slot_20: int
    value_slot_21: int
    value_slot_22: int
    value_slot_23: int
    value_slot_24: int

child_deck = [x for x in range(1, 61)] + [19, 20, 21, 22, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60] 

adol_deck = [x for x in range(61, 121)] + [79, 80, 81, 82, 119, 119, 119, 119, 119, 119, 119, 119, 120, 120, 120, 120, 120, 120, 120, 120] 

adult_deck = [x for x in range(121, 181)] + [139, 140, 141, 142, 179, 179, 179, 179, 179, 179, 179, 179, 180, 180, 180, 180, 180, 180, 180, 180]