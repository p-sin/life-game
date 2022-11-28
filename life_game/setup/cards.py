from typing import Union
from life_game.setup.definitions import BoardSlots as B, Attributes as A

CARDTYPE = dict[str,Union[B, dict[str, Union[int, A, None]]]]


dict[int, CARDTYPE]

cards = {
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
}
