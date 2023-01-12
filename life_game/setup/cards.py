from typing import Tuple
from life_game.setup.components import BoardSections as B, Attributes as A

card_type = dict[str, int | B | dict[str, str | A | None]]

cards: dict[int, card_type] = {
    1: {
        "number": 1,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    2: {
        "number": 2,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    3: {
        "number": 3,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    4: {
        "number": 4,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    5: {
        "number": 5,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    6: {
        "number": 6,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    7: {
        "number": 7,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    8: {
        "number": 8,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    9: {
        "number": 9,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    10: {
        "number": 10,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    11: {
        "number": 11,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    12: {
        "number": 12,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    13: {
        "number": 13,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    14: {
        "number": 14,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    15: {
        "number": 15,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    16: {
        "number": 16,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    17: {
        "number": 17,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    18: {
        "number": 18,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    19: {
        "number": 19,
        "board_section": B.BOARD_SECTION_THREE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_1,
            "values": A.EMPATHY_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    20: {
        "number": 20,
        "board_section": B.BOARD_SECTION_THREE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_1,
            "values": A.DETERM_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    21: {
        "number": 21,
        "board_section": B.BOARD_SECTION_THREE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_2,
            "values": A.EMPATHY_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    22: {
        "number": 22,
        "board_section": B.BOARD_SECTION_THREE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_2,
            "values": A.DETERM_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    23: {
        "number": 23,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.INTEL_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    24: {
        "number": 24,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.CREATE_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    25: {
        "number": 25,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.INTEL_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    26: {
        "number": 26,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.INTEL_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.CREATE_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    27: {
        "number": 27,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.CREATE_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    28: {
        "number": 28,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.CREATE_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.INTEL_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    29: {
        "number": 29,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.INTEL_ONE,
        },
    },
    30: {
        "number": 30,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.CREATE_ONE,
        },
    },
    31: {
        "number": 31,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.INTEL_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.SOCIAL_ONE,
        },
    },
    32: {
        "number": 32,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.INTEL_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.CREATE_ONE,
        },
    },
    33: {
        "number": 33,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.CREATE_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.SOCIAL_ONE,
        },
    },
    34: {
        "number": 34,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_1,
            "values": A.CREATE_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.INTEL_ONE,
        },
    },
    35: {
        "number": 35,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.INTEL_ONE,
        },
    },
    36: {
        "number": 36,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.SOCIAL_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.CREATE_ONE,
        },
    },
    37: {
        "number": 37,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.INTEL_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.SOCIAL_ONE,
        },
    },
    38: {
        "number": 38,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.INTEL_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.CREATE_ONE,
        },
    },
    39: {
        "number": 39,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.CREATE_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.SOCIAL_ONE,
        },
    },
    40: {
        "number": 40,
        "board_section": B.BOARD_SECTION_ONE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_2,
            "values": A.CREATE_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_ONE.value.card_slot_3,
            "values": A.INTEL_ONE,
        },
    },
    41: {
        "number": 41,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.CONST_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    42: {
        "number": 42,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.COORD_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    43: {
        "number": 43,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.CONST_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    44: {
        "number": 44,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.CONST_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.COORD_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    45: {
        "number": 45,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.COORD_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    46: {
        "number": 46,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.COORD_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.CONST_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    47: {
        "number": 47,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.CONST_ONE,
        },
    },
    48: {
        "number": 48,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.COORD_ONE,
        },
    },
    49: {
        "number": 49,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.CONST_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.STRENGTH_ONE,
        },
    },
    50: {
        "number": 50,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.CONST_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.COORD_ONE,
        },
    },
    51: {
        "number": 51,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.COORD_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.STRENGTH_ONE,
        },
    },
    52: {
        "number": 52,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_1,
            "values": A.COORD_ONE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.CONST_ONE,
        },
    },
    53: {
        "number": 53,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.CONST_ONE,
        },
    },
    54: {
        "number": 54,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.STRENGTH_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.COORD_ONE,
        },
    },
    55: {
        "number": 55,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.CONST_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.STRENGTH_ONE,
        },
    },
    56: {
        "number": 56,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.CONST_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.COORD_ONE,
        },
    },
    57: {
        "number": 57,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.COORD_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.STRENGTH_ONE,
        },
    },
    58: {
        "number": 58,
        "board_section": B.BOARD_SECTION_TWO,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_2,
            "values": A.COORD_ONE,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_TWO.value.card_slot_3,
            "values": A.CONST_ONE,
        },
    },
    59: {
        "number": 59,
        "board_section": B.BOARD_SECTION_THREE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_1,
            "values": A.DETERM_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_2,
            "values": A.EMPATHY_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    60: {
        "number": 60,
        "board_section": B.BOARD_SECTION_THREE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_1,
            "values": A.EMPATHY_ONE,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_THREE.value.card_slot_2,
            "values": A.DETERM_ONE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    61: {
        "number": 61,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.SOCIAL_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    62: {
        "number": 62,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.INTEL_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    63: {
        "number": 63,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.CREATE_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    64: {
        "number": 64,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.SOCIAL_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    65: {
        "number": 65,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.INTEL_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    66: {
        "number": 66,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.CREATE_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    67: {
        "number": 67,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.SOCIAL_THREE,
        },
    },
    68: {
        "number": 68,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.INTEL_THREE,
        },
    },
    69: {
        "number": 69,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.CREATE_THREE,
        },
    },
    70: {
        "number": 70,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.STRENGTH_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    71: {
        "number": 71,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.CONST_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    72: {
        "number": 72,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.COORD_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    73: {
        "number": 73,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.STRENGTH_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    74: {
        "number": 74,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.CONST_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    75: {
        "number": 75,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.COORD_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    76: {
        "number": 76,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.STRENGTH_THREE,
        },
    },
    77: {
        "number": 77,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.CONST_THREE,
        },
    },
    78: {
        "number": 78,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.COORD_THREE,
        },
    },
    79: {
        "number": 79,
        "board_section": B.BOARD_SECTION_SIX,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_1,
            "values": A.EMPATHY_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    80: {
        "number": 80,
        "board_section": B.BOARD_SECTION_SIX,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_1,
            "values": A.DETERM_THREE,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    81: {
        "number": 81,
        "board_section": B.BOARD_SECTION_SIX,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_2,
            "values": A.EMPATHY_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    82: {
        "number": 82,
        "board_section": B.BOARD_SECTION_SIX,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_2,
            "values": A.DETERM_THREE,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    83: {
        "number": 83,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    84: {
        "number": 84,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    85: {
        "number": 85,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    86: {
        "number": 86,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    87: {
        "number": 87,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    88: {
        "number": 88,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    89: {
        "number": 89,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    90: {
        "number": 90,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    91: {
        "number": 91,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    92: {
        "number": 92,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    93: {
        "number": 93,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    94: {
        "number": 94,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    95: {
        "number": 95,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    96: {
        "number": 96,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    97: {
        "number": 97,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    98: {
        "number": 98,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    99: {
        "number": 99,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    100: {
        "number": 100,
        "board_section": B.BOARD_SECTION_FOUR,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FOUR.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    101: {
        "number": 101,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    102: {
        "number": 102,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    103: {
        "number": 103,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    104: {
        "number": 104,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    105: {
        "number": 105,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    106: {
        "number": 106,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    107: {
        "number": 107,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    108: {
        "number": 108,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    109: {
        "number": 109,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    110: {
        "number": 110,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    111: {
        "number": 111,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    112: {
        "number": 112,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    113: {
        "number": 113,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    114: {
        "number": 114,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    115: {
        "number": 115,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    116: {
        "number": 116,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    117: {
        "number": 117,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    118: {
        "number": 118,
        "board_section": B.BOARD_SECTION_FIVE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_FIVE.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    119: {
        "number": 119,
        "board_section": B.BOARD_SECTION_SIX,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_1,
            "values": A.DETERM_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_2,
            "values": A.EMPATHY_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    120: {
        "number": 120,
        "board_section": B.BOARD_SECTION_SIX,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_1,
            "values": A.EMPATHY_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SIX.value.card_slot_2,
            "values": A.DETERM_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    121: {
        "number": 121,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.SOCIAL_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    122: {
        "number": 122,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.INTEL_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    123: {
        "number": 123,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.CREATE_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    124: {
        "number": 124,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.SOCIAL_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    125: {
        "number": 125,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.INTEL_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    126: {
        "number": 126,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.CREATE_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    127: {
        "number": 127,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.SOCIAL_FOUR,
        },
    },
    128: {
        "number": 128,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.INTEL_FOUR,
        },
    },
    129: {
        "number": 129,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.CREATE_FOUR,
        },
    },
    130: {
        "number": 130,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.STRENGTH_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    131: {
        "number": 131,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.CONST_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    132: {
        "number": 132,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.COORD_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    133: {
        "number": 133,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.STRENGTH_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    134: {
        "number": 134,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.CONST_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    135: {
        "number": 135,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.COORD_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    136: {
        "number": 136,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.STRENGTH_FOUR,
        },
    },
    137: {
        "number": 137,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.CONST_FOUR,
        },
    },
    138: {
        "number": 138,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.COORD_FOUR,
        },
    },
    139: {
        "number": 139,
        "board_section": B.BOARD_SECTION_NINE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_1,
            "values": A.EMPATHY_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    140: {
        "number": 140,
        "board_section": B.BOARD_SECTION_NINE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_1,
            "values": A.DETERM_FOUR,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    141: {
        "number": 141,
        "board_section": B.BOARD_SECTION_NINE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_2,
            "values": A.EMPATHY_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    142: {
        "number": 142,
        "board_section": B.BOARD_SECTION_NINE,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_2,
            "values": A.DETERM_FOUR,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    143: {
        "number": 143,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    144: {
        "number": 144,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    145: {
        "number": 145,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    146: {
        "number": 146,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    147: {
        "number": 147,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    148: {
        "number": 148,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    149: {
        "number": 149,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    150: {
        "number": 150,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    151: {
        "number": 151,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    152: {
        "number": 152,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.INTEL_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    153: {
        "number": 153,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    154: {
        "number": 154,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_1,
            "values": A.CREATE_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    155: {
        "number": 155,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    156: {
        "number": 156,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.SOCIAL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    157: {
        "number": 157,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    158: {
        "number": 158,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.INTEL_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.CREATE_TWO,
        },
    },
    159: {
        "number": 159,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.SOCIAL_TWO,
        },
    },
    160: {
        "number": 160,
        "board_section": B.BOARD_SECTION_SEVEN,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_2,
            "values": A.CREATE_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_SEVEN.value.card_slot_3,
            "values": A.INTEL_TWO,
        },
    },
    161: {
        "number": 161,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    162: {
        "number": 162,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    163: {
        "number": 163,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    164: {
        "number": 164,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    165: {
        "number": 165,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    166: {
        "number": 166,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    167: {
        "number": 167,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    168: {
        "number": 168,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    169: {
        "number": 169,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    170: {
        "number": 170,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.CONST_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    171: {
        "number": 171,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    172: {
        "number": 172,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_1,
            "values": A.COORD_TWO,
        },
        "card_slot_2": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    173: {
        "number": 173,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    174: {
        "number": 174,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.STRENGTH_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    175: {
        "number": 175,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    176: {
        "number": 176,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.CONST_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.COORD_TWO,
        },
    },
    177: {
        "number": 177,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.STRENGTH_TWO,
        },
    },
    178: {
        "number": 178,
        "board_section": B.BOARD_SECTION_EIGHT,
        "card_slot_1": {
            "slot_number": None,
            "values": None,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_2,
            "values": A.COORD_TWO,
        },
        "card_slot_3": {
            "slot_number": B.BOARD_SECTION_EIGHT.value.card_slot_3,
            "values": A.CONST_TWO,
        },
    },
    179: {
        "number": 179,
        "board_section": B.BOARD_SECTION_NINE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_1,
            "values": A.DETERM_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_2,
            "values": A.EMPATHY_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
    180: {
        "number": 180,
        "board_section": B.BOARD_SECTION_NINE,
        "card_slot_1": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_1,
            "values": A.EMPATHY_TWO,
        },
        "card_slot_2": {
            "slot_number": B.BOARD_SECTION_NINE.value.card_slot_2,
            "values": A.DETERM_TWO,
        },
        "card_slot_3": {
            "slot_number": None,
            "values": None,
        },
    },
}
