from typing import Union
from life_game.setup.components import BoardSections as B, Attributes as A

CARDTYPE = dict[str,Union[B, dict[str, Union[int, A, None]]]]

cards: dict[int, CARDTYPE] = {
    1: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    2: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    3: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    4: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    5: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    6: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    7: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    8: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    9: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    10: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    11: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    12: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    13: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    14: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    15: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    16: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    17: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    18: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    19: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_THREE,
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
    20: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_THREE,
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
    21: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_THREE,
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
    22: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_THREE,
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
    23: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    24: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    25: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    26: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    27: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    28: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    29: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    30: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    31: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    32: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    33: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    34: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    35: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    36: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    37: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    38: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    39: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    40: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_ONE,
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
    41: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    42: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    43: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    44: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    45: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    46: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    47: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    48: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    49: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    50: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    51: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    52: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    53: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    54: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    55: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    56: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    57: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    58: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_TWO,
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
    59: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_THREE,
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
    60: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_THREE,
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
    61: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    62: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    63: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    64: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    65: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    66: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    67: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    68: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    69: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    70: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    71: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    72: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    73: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    74: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    75: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    76: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    77: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    78: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    79: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SIX,
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
    80: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SIX,
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
    81: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SIX,
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
    82: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SIX,
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
    83: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    84: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    85: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    86: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    87: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    88: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    89: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    90: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    91: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    92: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    93: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    94: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    95: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    96: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    97: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    98: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    99: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    100: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FOUR,
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
    101: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    102: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    103: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    104: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    105: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    106: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    107: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    108: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    109: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    110: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    111: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    112: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    113: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    114: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    115: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    116: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    117: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    118: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_FIVE,
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
    119: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SIX,
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
    120: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SIX,
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
   121: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    122: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    123: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    124: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    125: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    126: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    127: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    128: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    129: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    130: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    131: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    132: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    133: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    134: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    135: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    136: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    137: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    138: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    139: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_NINE,
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
    140: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_NINE,
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
    141: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_NINE,
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
    142: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_NINE,
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
    143: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    144: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    145: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    146: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    147: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    148: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    149: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    150: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    151: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    152: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    153: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    154: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    155: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    156: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    157: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    158: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    159: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    160: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_SEVEN,
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
    161: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    162: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    163: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    164: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    165: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    166: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    167: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    168: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    169: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    170: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    171: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    172: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    173: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    174: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    175: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    176: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    177: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    178: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_EIGHT,
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
    179: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_NINE,
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
    180: 
        {
            "BOARD_SECTION": B.BOARD_SECTION_NINE,
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
