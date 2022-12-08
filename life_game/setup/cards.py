from typing import Union
from life_game.setup.definitions import BoardSlots as B, Attributes as A

CARDTYPE = dict[str,Union[B, dict[str, Union[int, A, None]]]]

cards: dict[int, CARDTYPE] = {
    1: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    5: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    6: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    7: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    8: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    9: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },    
    10: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    14: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    15: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    16: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    17: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },
    18: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    19: 
        {
            "board_slot": B.BOARD_SLOT_THREE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_THREE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_THREE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_2,
                "values": A.EMPATHY_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    22: 
        {
            "board_slot": B.BOARD_SLOT_THREE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_2,
                "values": A.DETERM_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    23: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.INTEL_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    24: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.CREATE_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    25: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.INTEL_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    26: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.INTEL_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.CREATE_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    27: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.CREATE_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    28: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.CREATE_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.INTEL_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    29: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.INTEL_ONE,
            },
        },
    30: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.CREATE_ONE,
            },
        },
    31: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.INTEL_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.SOCIAL_ONE,
            },
        },
    32: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.INTEL_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.CREATE_ONE,
            },
        },
    33: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.CREATE_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.SOCIAL_ONE,
            },
        },
    34: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_1,
                "values": A.CREATE_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.INTEL_ONE,
            },
        }, 
    35: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.INTEL_ONE,
            },
        },
    36: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.SOCIAL_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.CREATE_ONE,
            },
        },
    37: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.INTEL_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.SOCIAL_ONE,
            },
        },
    38: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.INTEL_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.CREATE_ONE,
            },
        },
    39: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.CREATE_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.SOCIAL_ONE,
            },
        },
    40: 
        {
            "board_slot": B.BOARD_SLOT_ONE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_2,
                "values": A.CREATE_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_ONE.value.card_slot_3,
                "values": A.INTEL_ONE,
            },
        },
    41: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.CONST_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    42: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.COORD_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    43: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.CONST_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    44: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.CONST_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.COORD_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    45: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.COORD_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    46: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.COORD_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.CONST_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    47: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.CONST_ONE,
            },
        },
    48: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.COORD_ONE,
            },
        },
    49: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.CONST_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.STRENGTH_ONE,
            },
        },
    50: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.CONST_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.COORD_ONE,
            },
        },
    51: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.COORD_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.STRENGTH_ONE,
            },
        },
    52: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_1,
                "values": A.COORD_ONE,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.CONST_ONE,
            },
        },     
    53: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.CONST_ONE,
            },
        },
    54: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.STRENGTH_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.COORD_ONE,
            },
        },
    55: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.CONST_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.STRENGTH_ONE,
            },
        },
    56: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.CONST_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.COORD_ONE,
            },
        },
    57: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.COORD_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.STRENGTH_ONE,
            },
        },
    58: 
        {
            "board_slot": B.BOARD_SLOT_TWO,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_2,
                "values": A.COORD_ONE,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_TWO.value.card_slot_3,
                "values": A.CONST_ONE,
            },
        },   
    59: 
        {
            "board_slot": B.BOARD_SLOT_THREE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_1,
                "values": A.DETERM_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_2,
                "values": A.EMPATHY_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    60: 
        {
            "board_slot": B.BOARD_SLOT_THREE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_1,
                "values": A.EMPATHY_ONE,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_THREE.value.card_slot_2,
                "values": A.DETERM_ONE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    61: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.SOCIAL_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    65: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.INTEL_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    66: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.CREATE_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    67: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.SOCIAL_THREE,
            },
        },
    68: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.INTEL_THREE,
            },
        },
    69: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.CREATE_THREE,
            },
        },    
    70: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.STRENGTH_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    74: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.CONST_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    75: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.COORD_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    76: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.STRENGTH_THREE,
            },
        },
    77: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.CONST_THREE,
            },
        },
    78: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.COORD_THREE,
            },
        },
    79: 
        {
            "board_slot": B.BOARD_SLOT_SIX,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_SIX,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_SIX,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_2,
                "values": A.EMPATHY_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    82: 
        {
            "board_slot": B.BOARD_SLOT_SIX,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_2,
                "values": A.DETERM_THREE,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    83: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    84: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    85: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    86: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    87: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    88: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    89: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    90: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    91: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    92: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    93: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    94: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        }, 
    95: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    96: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    97: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    98: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    99: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    100: 
        {
            "board_slot": B.BOARD_SLOT_FOUR,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FOUR.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    101: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    102: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    103: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    104: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    105: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    106: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    107: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },
    108: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    109: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    110: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    111: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    112: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },     
    113: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },
    114: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    115: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    116: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    117: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    118: 
        {
            "board_slot": B.BOARD_SLOT_FIVE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_FIVE.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },   
    119: 
        {
            "board_slot": B.BOARD_SLOT_SIX,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_1,
                "values": A.DETERM_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_2,
                "values": A.EMPATHY_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    120: 
        {
            "board_slot": B.BOARD_SLOT_SIX,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_1,
                "values": A.EMPATHY_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SIX.value.card_slot_2,
                "values": A.DETERM_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
   121: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.SOCIAL_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    125: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.INTEL_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    126: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.CREATE_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    127: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.SOCIAL_FOUR,
            },
        },
    128: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.INTEL_FOUR,
            },
        },
    129: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.CREATE_FOUR,
            },
        },    
    130: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.STRENGTH_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    134: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.CONST_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    135: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.COORD_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    136: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.STRENGTH_FOUR,
            },
        },
    137: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.CONST_FOUR,
            },
        },
    138: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.COORD_FOUR,
            },
        },
    139: 
        {
            "board_slot": B.BOARD_SLOT_NINE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_NINE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_1,
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
            "board_slot": B.BOARD_SLOT_NINE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_2,
                "values": A.EMPATHY_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    142: 
        {
            "board_slot": B.BOARD_SLOT_NINE,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_2,
                "values": A.DETERM_FOUR,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    143: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    144: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    145: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    146: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    147: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    148: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    149: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    150: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    151: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    152: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.INTEL_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    153: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    154: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_1,
                "values": A.CREATE_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        }, 
    155: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    156: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.SOCIAL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    157: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    158: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.INTEL_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.CREATE_TWO,
            },
        },
    159: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.SOCIAL_TWO,
            },
        },
    160: 
        {
            "board_slot": B.BOARD_SLOT_SEVEN,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_2,
                "values": A.CREATE_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_SEVEN.value.card_slot_3,
                "values": A.INTEL_TWO,
            },
        },
    161: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    162: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    163: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    164: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    165: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    166: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    167: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },
    168: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    169: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    170: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.CONST_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    171: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    172: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_1,
                "values": A.COORD_TWO,
            },
            "card_slot_2": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },     
    173: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },
    174: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.STRENGTH_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    175: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    176: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.CONST_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.COORD_TWO,
            },
        },
    177: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.STRENGTH_TWO,
            },
        },
    178: 
        {
            "board_slot": B.BOARD_SLOT_EIGHT,
            "card_slot_1": {
                "slot_number": None,
                "values": None,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_2,
                "values": A.COORD_TWO,
            },
            "card_slot_3": {
                "slot_number": B.BOARD_SLOT_EIGHT.value.card_slot_3,
                "values": A.CONST_TWO,
            },
        },   
    179: 
        {
            "board_slot": B.BOARD_SLOT_NINE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_1,
                "values": A.DETERM_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_2,
                "values": A.EMPATHY_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
    180: 
        {
            "board_slot": B.BOARD_SLOT_NINE,
            "card_slot_1": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_1,
                "values": A.EMPATHY_TWO,
            },
            "card_slot_2": {
                "slot_number": B.BOARD_SLOT_NINE.value.card_slot_2,
                "values": A.DETERM_TWO,
            },
            "card_slot_3": {
                "slot_number": None,
                "values": None,
            },
        },
}
