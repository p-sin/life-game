from enum import Enum
from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class AttributeInfo:
    name: str
    value: int


class Attributes(Enum):
    SOCIAL_ONE = AttributeInfo(
        name="Sociability",
        value=1,
    )
    SOCIAL_TWO = AttributeInfo(
        name="Sociability",
        value=2,
    )
    SOCIAL_THREE = AttributeInfo(
        name="Sociability",
        value=3,
    )
    SOCIAL_FOUR = AttributeInfo(
        name="Sociability",
        value=4,
    )
    INTEL_ONE = AttributeInfo(
        name="Intelligence",
        value=1,
    )
    INTEL_TWO = AttributeInfo(
        name="Intelligence",
        value=2,
    )
    INTEL_THREE = AttributeInfo(
        name="Intelligence",
        value=3,
    )
    INTEL_FOUR = AttributeInfo(
        name="Intelligence",
        value=4,
    )
    CREATE_ONE = AttributeInfo(
        name="Creativity",
        value=1,
    )
    CREATE_TWO = AttributeInfo(
        name="Creativity",
        value=2,
    )
    CREATE_THREE = AttributeInfo(
        name="Creativity",
        value=3,
    )
    CREATE_FOUR = AttributeInfo(
        name="Creativity",
        value=4,
    )
    STRENGTH_ONE = AttributeInfo(
        name="Strength",
        value=1,
    )
    STRENGTH_TWO = AttributeInfo(
        name="Strength",
        value=2,
    )
    STRENGTH_THREE = AttributeInfo(
        name="Strength",
        value=3,
    )
    STRENGTH_FOUR = AttributeInfo(
        name="Strength",
        value=4,
    )
    CONST_ONE = AttributeInfo(
        name="Constitution",
        value=1,
    )
    CONST_TWO = AttributeInfo(
        name="Constitution",
        value=2,
    )
    CONST_THREE = AttributeInfo(
        name="Constitution",
        value=3,
    )
    CONST_FOUR = AttributeInfo(
        name="Constitution",
        value=4,
    )
    COORD_ONE = AttributeInfo(
        name="Co-ordination",
        value=1,
    )
    COORD_TWO = AttributeInfo(
        name="Co-ordination",
        value=2,
    )
    COORD_THREE = AttributeInfo(
        name="Co-ordination",
        value=3,
    )
    COORD_FOUR = AttributeInfo(
        name="Co-ordination",
        value=4,
    )
    EMPATHY_ONE = AttributeInfo(
        name="Empathy",
        value=1,
    )
    EMPATHY_TWO = AttributeInfo(
        name="Empathy",
        value=2,
    )
    EMPATHY_THREE = AttributeInfo(
        name="Empathy",
        value=3,
    )
    EMPATHY_FOUR = AttributeInfo(
        name="Empathy",
        value=4,
    )
    DETERM_ONE = AttributeInfo(
        name="Determination",
        value=1,
    )
    DETERM_TWO = AttributeInfo(
        name="Determination",
        value=2,
    )
    DETERM_THREE = AttributeInfo(
        name="Determination",
        value=3,
    )
    DETERM_FOUR = AttributeInfo(
        name="Determination",
        value=4,
    )


@dataclass
class BoardSectionInfo:
    number: int
    body_part: str
    life_stage: str
    card_slot_1: str
    card_slot_2: str
    card_slot_3: Optional[str] = None


class BoardSections(Enum):
    BOARD_SECTION_ONE = BoardSectionInfo(
        number=1,
        body_part="mind",
        life_stage="child",
        card_slot_1="attr_slot_1",
        card_slot_2="attr_slot_2",
        card_slot_3="attr_slot_3",
    )
    BOARD_SECTION_TWO = BoardSectionInfo(
        number=2,
        body_part="body",
        life_stage="child",
        card_slot_1="attr_slot_4",
        card_slot_2="attr_slot_5",
        card_slot_3="attr_slot_6",
    )
    BOARD_SECTION_THREE = BoardSectionInfo(
        number=3,
        body_part="soul",
        life_stage="child",
        card_slot_1="attr_slot_7",
        card_slot_2="attr_slot_8",
        card_slot_3=None,
    )
    BOARD_SECTION_FOUR = BoardSectionInfo(
        number=4,
        body_part="mind",
        life_stage="adolescent",
        card_slot_1="attr_slot_9",
        card_slot_2="attr_slot_10",
        card_slot_3="attr_slot_11",
    )
    BOARD_SECTION_FIVE = BoardSectionInfo(
        number=5,
        body_part="body",
        life_stage="adolescent",
        card_slot_1="attr_slot_12",
        card_slot_2="attr_slot_13",
        card_slot_3="attr_slot_14",
    )
    BOARD_SECTION_SIX = BoardSectionInfo(
        number=6,
        body_part="soul",
        life_stage="adolescent",
        card_slot_1="attr_slot_15",
        card_slot_2="attr_slot_16",
        card_slot_3=None,
    )
    BOARD_SECTION_SEVEN = BoardSectionInfo(
        number=7,
        body_part="mind",
        life_stage="adult",
        card_slot_1="attr_slot_17",
        card_slot_2="attr_slot_18",
        card_slot_3="attr_slot_19",
    )
    BOARD_SECTION_EIGHT = BoardSectionInfo(
        number=8,
        body_part="body",
        life_stage="adult",
        card_slot_1="attr_slot_20",
        card_slot_2="attr_slot_21",
        card_slot_3="attr_slot_22",
    )
    BOARD_SECTION_NINE = BoardSectionInfo(
        number=9,
        body_part="soul",
        life_stage="adult",
        card_slot_1="attr_slot_23",
        card_slot_2="attr_slot_24",
        card_slot_3=None,
    )


attribute_slots: dict[str, dict[str, Union[str, int]]] = {
    "attr_slot_1": {
        "type": "",
        "value": 0,
    },
    "attr_slot_2": {
        "type": "",
        "value": 0,
    },
    "attr_slot_3": {
        "type": "",
        "value": 0,
    },
    "attr_slot_4": {
        "type": "",
        "value": 0,
    },
    "attr_slot_5": {
        "type": "",
        "value": 0,
    },
    "attr_slot_6": {
        "type": "",
        "value": 0,
    },
    "attr_slot_7": {
        "type": "",
        "value": 0,
    },
    "attr_slot_8": {
        "type": "",
        "value": 0,
    },
    "attr_slot_9": {
        "type": "",
        "value": 0,
    },
    "attr_slot_10": {
        "type": "",
        "value": 0,
    },
    "attr_slot_11": {
        "type": "",
        "value": 0,
    },
    "attr_slot_12": {
        "type": "",
        "value": 0,
    },
    "attr_slot_13": {
        "type": "",
        "value": 0,
    },
    "attr_slot_14": {
        "type": "",
        "value": 0,
    },
    "attr_slot_15": {
        "type": "",
        "value": 0,
    },
    "attr_slot_16": {
        "type": "",
        "value": 0,
    },
    "attr_slot_17": {
        "type": "",
        "value": 0,
    },
    "attr_slot_18": {
        "type": "",
        "value": 0,
    },
    "attr_slot_19": {
        "type": "",
        "value": 0,
    },
    "attr_slot_20": {
        "type": "",
        "value": 0,
    },
    "attr_slot_21": {
        "type": "",
        "value": 0,
    },
    "attr_slot_22": {
        "type": "",
        "value": 0,
    },
    "attr_slot_23": {
        "type": "",
        "value": 0,
    },
    "attr_slot_24": {
        "type": "",
        "value": 0,
    },
}


@dataclass
class Board:
    """Defines the playerboard"""

    player: int
    attribute_slots: dict[str, dict[str, Union[str, int]]]
    sociability: int = 0
    intelligence: int = 0
    creativity: int = 0
    strength: int = 0
    constitution: int = 0
    coordination: int = 0
    empathy: int = 0
    determination: int = 0


decks = {
    "child": [x for x in range(1, 61)]
    + [19, 20, 21, 22, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60],
    "adol": [x for x in range(61, 121)]
    + [
        79,
        80,
        81,
        82,
        119,
        119,
        119,
        119,
        119,
        119,
        119,
        119,
        120,
        120,
        120,
        120,
        120,
        120,
        120,
        120,
    ],
    "adult": [x for x in range(121, 181)]
    + [
        139,
        140,
        141,
        142,
        179,
        179,
        179,
        179,
        179,
        179,
        179,
        179,
        180,
        180,
        180,
        180,
        180,
        180,
        180,
        180,
    ],
}

rounds = ["child", "adol", "adult"]
