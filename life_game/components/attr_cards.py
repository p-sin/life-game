from life_game.components.constants import Attributes as A
from life_game.components.constants import BoardSlots as B

card_config: dict[int, dict[str, B | list[A]]] = {
    1: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_TWO, A.NONE, A.NONE],
    },
    2: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_TWO, A.NONE, A.NONE],
    },
    3: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_TWO, A.NONE, A.NONE],
    },
    4: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.SOCIAL_TWO, A.NONE],
    },
    5: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.INTEL_TWO, A.NONE],
    },
    6: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.CREATE_TWO, A.NONE],
    },
    7: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.NONE, A.SOCIAL_TWO],
    },
    8: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.NONE, A.INTEL_TWO],
    },
    9: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.NONE, A.CREATE_TWO],
    },
    10: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_TWO, A.NONE, A.NONE],
    },
    11: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_TWO, A.NONE, A.NONE],
    },
    12: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_TWO, A.NONE, A.NONE],
    },
    13: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.STRENGTH_TWO, A.NONE],
    },
    14: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.CONST_TWO, A.NONE],
    },
    15: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.COORD_TWO, A.NONE],
    },
    16: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.NONE, A.STRENGTH_TWO],
    },
    17: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.NONE, A.CONST_TWO],
    },
    18: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.NONE, A.COORD_TWO],
    },
    19: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.EMPATHY_TWO, A.NONE, A.NONE],
    },
    20: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.DETERM_TWO, A.NONE, A.NONE],
    },
    21: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.NONE, A.EMPATHY_TWO, A.NONE],
    },
    22: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.NONE, A.DETERM_TWO, A.NONE],
    },
    23: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, A.INTEL_ONE, A.NONE],
    },
    24: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, A.CREATE_ONE, A.NONE],
    },
    25: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, A.SOCIAL_ONE, A.NONE],
    },
    26: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, A.CREATE_ONE, A.NONE],
    },
    27: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, A.SOCIAL_ONE, A.NONE],
    },
    28: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, A.INTEL_ONE, A.NONE],
    },
    29: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, A.NONE, A.INTEL_ONE],
    },
    30: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, A.NONE, A.CREATE_ONE],
    },
    31: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, A.NONE, A.SOCIAL_ONE],
    },
    32: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, A.NONE, A.CREATE_ONE],
    },
    33: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, A.NONE, A.SOCIAL_ONE],
    },
    34: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, A.NONE, A.INTEL_ONE],
    },
    35: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.SOCIAL_ONE, A.INTEL_ONE],
    },
    36: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.SOCIAL_ONE, A.CREATE_ONE],
    },
    37: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.INTEL_ONE, A.SOCIAL_ONE],
    },
    38: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.INTEL_ONE, A.CREATE_ONE],
    },
    39: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.CREATE_ONE, A.SOCIAL_ONE],
    },
    40: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.NONE, A.CREATE_ONE, A.INTEL_ONE],
    },
    41: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, A.CONST_ONE, A.NONE],
    },
    42: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, A.COORD_ONE, A.NONE],
    },
    43: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, A.STRENGTH_ONE, A.NONE],
    },
    44: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, A.COORD_ONE, A.NONE],
    },
    45: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, A.STRENGTH_ONE, A.NONE],
    },
    46: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, A.CONST_ONE, A.NONE],
    },
    47: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, A.NONE, A.CONST_ONE],
    },
    48: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, A.NONE, A.COORD_ONE],
    },
    49: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, A.NONE, A.STRENGTH_ONE],
    },
    50: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, A.NONE, A.COORD_ONE],
    },
    51: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, A.NONE, A.STRENGTH_ONE],
    },
    52: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, A.NONE, A.CONST_ONE],
    },
    53: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.STRENGTH_ONE, A.CONST_ONE],
    },
    54: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.STRENGTH_ONE, A.COORD_ONE],
    },
    55: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.CONST_ONE, A.STRENGTH_ONE],
    },
    56: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.CONST_ONE, A.COORD_ONE],
    },
    57: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.COORD_ONE, A.STRENGTH_ONE],
    },
    58: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.NONE, A.COORD_ONE, A.CONST_ONE],
    },
    59: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.DETERM_ONE, A.EMPATHY_ONE, A.NONE],
    },
    60: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.EMPATHY_ONE, A.DETERM_ONE, A.NONE],
    },
    61: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_THREE, A.NONE, A.NONE],
    },
    62: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_THREE, A.NONE, A.NONE],
    },
    63: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_THREE, A.NONE, A.NONE],
    },
    64: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.SOCIAL_THREE, A.NONE],
    },
    65: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.INTEL_THREE, A.NONE],
    },
    66: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.CREATE_THREE, A.NONE],
    },
    67: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.NONE, A.SOCIAL_THREE],
    },
    68: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.NONE, A.INTEL_THREE],
    },
    69: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.NONE, A.CREATE_THREE],
    },
    70: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_THREE, A.NONE, A.NONE],
    },
    71: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_THREE, A.NONE, A.NONE],
    },
    72: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_THREE, A.NONE, A.NONE],
    },
    73: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.STRENGTH_THREE, A.NONE],
    },
    74: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.CONST_THREE, A.NONE],
    },
    75: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.COORD_THREE, A.NONE],
    },
    76: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.NONE, A.STRENGTH_THREE],
    },
    77: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.NONE, A.CONST_THREE],
    },
    78: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.NONE, A.COORD_THREE],
    },
    79: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.EMPATHY_THREE, A.NONE, A.NONE],
    },
    80: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.DETERM_THREE, A.NONE, A.NONE],
    },
    81: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.NONE, A.EMPATHY_THREE, A.NONE],
    },
    82: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.NONE, A.DETERM_THREE, A.NONE],
    },
    83: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, A.INTEL_TWO, A.NONE],
    },
    84: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, A.CREATE_TWO, A.NONE],
    },
    85: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, A.SOCIAL_TWO, A.NONE],
    },
    86: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, A.CREATE_TWO, A.NONE],
    },
    87: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, A.SOCIAL_TWO, A.NONE],
    },
    88: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, A.INTEL_TWO, A.NONE],
    },
    89: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, A.NONE, A.INTEL_TWO],
    },
    90: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, A.NONE, A.CREATE_TWO],
    },
    91: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, A.NONE, A.SOCIAL_TWO],
    },
    92: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, A.NONE, A.CREATE_TWO],
    },
    93: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, A.NONE, A.SOCIAL_TWO],
    },
    94: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, A.NONE, A.INTEL_TWO],
    },
    95: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.SOCIAL_TWO, A.INTEL_TWO],
    },
    96: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.SOCIAL_TWO, A.CREATE_TWO],
    },
    97: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.INTEL_TWO, A.SOCIAL_TWO],
    },
    98: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.INTEL_TWO, A.CREATE_TWO],
    },
    99: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.CREATE_TWO, A.SOCIAL_TWO],
    },
    100: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.NONE, A.CREATE_TWO, A.INTEL_TWO],
    },
    101: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, A.CONST_TWO, A.NONE],
    },
    102: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, A.COORD_TWO, A.NONE],
    },
    103: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, A.STRENGTH_TWO, A.NONE],
    },
    104: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, A.COORD_TWO, A.NONE],
    },
    105: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, A.STRENGTH_TWO, A.NONE],
    },
    106: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, A.CONST_TWO, A.NONE],
    },
    107: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, A.NONE, A.CONST_TWO],
    },
    108: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, A.NONE, A.COORD_TWO],
    },
    109: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, A.NONE, A.STRENGTH_TWO],
    },
    110: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, A.NONE, A.COORD_TWO],
    },
    111: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, A.NONE, A.STRENGTH_TWO],
    },
    112: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, A.NONE, A.CONST_TWO],
    },
    113: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.STRENGTH_TWO, A.CONST_TWO],
    },
    114: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.STRENGTH_TWO, A.COORD_TWO],
    },
    115: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.CONST_TWO, A.STRENGTH_TWO],
    },
    116: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.CONST_TWO, A.COORD_TWO],
    },
    117: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.COORD_TWO, A.STRENGTH_TWO],
    },
    118: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.NONE, A.COORD_TWO, A.CONST_TWO],
    },
    119: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.DETERM_TWO, A.EMPATHY_TWO, A.NONE],
    },
    120: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.EMPATHY_TWO, A.DETERM_TWO, A.NONE],
    },
    121: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_FOUR, A.NONE, A.NONE],
    },
    122: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_FOUR, A.NONE, A.NONE],
    },
    123: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_FOUR, A.NONE, A.NONE],
    },
    124: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.SOCIAL_FOUR, A.NONE],
    },
    125: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.INTEL_FOUR, A.NONE],
    },
    126: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.CREATE_FOUR, A.NONE],
    },
    127: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.NONE, A.SOCIAL_FOUR],
    },
    128: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.NONE, A.INTEL_FOUR],
    },
    129: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.NONE, A.CREATE_FOUR],
    },
    130: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_FOUR, A.NONE, A.NONE],
    },
    131: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_FOUR, A.NONE, A.NONE],
    },
    132: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_FOUR, A.NONE, A.NONE],
    },
    133: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.STRENGTH_FOUR, A.NONE],
    },
    134: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.CONST_FOUR, A.NONE],
    },
    135: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.COORD_FOUR, A.NONE],
    },
    136: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.NONE, A.STRENGTH_FOUR],
    },
    137: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.NONE, A.CONST_FOUR],
    },
    138: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.NONE, A.COORD_FOUR],
    },
    139: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.EMPATHY_FOUR, A.NONE, A.NONE],
    },
    140: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.DETERM_FOUR, A.NONE, A.NONE],
    },
    141: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.NONE, A.EMPATHY_FOUR, A.NONE],
    },
    142: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.NONE, A.DETERM_FOUR, A.NONE],
    },
    143: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, A.INTEL_TWO, A.NONE],
    },
    144: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, A.CREATE_TWO, A.NONE],
    },
    145: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, A.SOCIAL_TWO, A.NONE],
    },
    146: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, A.CREATE_TWO, A.NONE],
    },
    147: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, A.SOCIAL_TWO, A.NONE],
    },
    148: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, A.INTEL_TWO, A.NONE],
    },
    149: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, A.NONE, A.INTEL_TWO],
    },
    150: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, A.NONE, A.CREATE_TWO],
    },
    151: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, A.NONE, A.SOCIAL_TWO],
    },
    152: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, A.NONE, A.CREATE_TWO],
    },
    153: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, A.NONE, A.SOCIAL_TWO],
    },
    154: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, A.NONE, A.INTEL_TWO],
    },
    155: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.SOCIAL_TWO, A.INTEL_TWO],
    },
    156: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.SOCIAL_TWO, A.CREATE_TWO],
    },
    157: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.INTEL_TWO, A.SOCIAL_TWO],
    },
    158: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.INTEL_TWO, A.CREATE_TWO],
    },
    159: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.CREATE_TWO, A.SOCIAL_TWO],
    },
    160: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.NONE, A.CREATE_TWO, A.INTEL_TWO],
    },
    161: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, A.CONST_TWO, A.NONE],
    },
    162: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, A.COORD_TWO, A.NONE],
    },
    163: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, A.STRENGTH_TWO, A.NONE],
    },
    164: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, A.COORD_TWO, A.NONE],
    },
    165: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, A.STRENGTH_TWO, A.NONE],
    },
    166: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, A.CONST_TWO, A.NONE],
    },
    167: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, A.NONE, A.CONST_TWO],
    },
    168: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, A.NONE, A.COORD_TWO],
    },
    169: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, A.NONE, A.STRENGTH_TWO],
    },
    170: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, A.NONE, A.COORD_TWO],
    },
    171: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, A.NONE, A.STRENGTH_TWO],
    },
    172: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, A.NONE, A.CONST_TWO],
    },
    173: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.STRENGTH_TWO, A.CONST_TWO],
    },
    174: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.STRENGTH_TWO, A.COORD_TWO],
    },
    175: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.CONST_TWO, A.STRENGTH_TWO],
    },
    176: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.CONST_TWO, A.COORD_TWO],
    },
    177: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.COORD_TWO, A.STRENGTH_TWO],
    },
    178: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.NONE, A.COORD_TWO, A.CONST_TWO],
    },
    179: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.DETERM_TWO, A.EMPATHY_TWO, A.NONE],
    },
    180: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.EMPATHY_TWO, A.DETERM_TWO, A.NONE],
    },
}
