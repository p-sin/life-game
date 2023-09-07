from life_game.setup.components import Attributes as A
from life_game.setup.components import BoardSlots as B

cards: dict[int, dict[str, B | list[A | None]]] = {
    1: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_TWO, None, None],
    },
    2: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_TWO, None, None],
    },
    3: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_TWO, None, None],
    },
    4: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.SOCIAL_TWO, None],
    },
    5: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.INTEL_TWO, None],
    },
    6: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.CREATE_TWO, None],
    },
    7: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, None, A.SOCIAL_TWO],
    },
    8: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, None, A.INTEL_TWO],
    },
    9: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, None, A.CREATE_TWO],
    },
    10: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_TWO, None, None],
    },
    11: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_TWO, None, None],
    },
    12: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_TWO, None, None],
    },
    13: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.STRENGTH_TWO, None],
    },
    14: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.CONST_TWO, None],
    },
    15: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.COORD_TWO, None],
    },
    16: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, None, A.STRENGTH_TWO],
    },
    17: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, None, A.CONST_TWO],
    },
    18: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, None, A.COORD_TWO],
    },
    19: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.EMPATHY_TWO, None, None],
    },
    20: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.DETERM_TWO, None, None],
    },
    21: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [None, A.EMPATHY_TWO, None],
    },
    22: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [None, A.DETERM_TWO, None],
    },
    23: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, A.INTEL_ONE, None],
    },
    24: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, A.CREATE_ONE, None],
    },
    25: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, A.SOCIAL_ONE, None],
    },
    26: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, A.CREATE_ONE, None],
    },
    27: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, A.SOCIAL_ONE, None],
    },
    28: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, A.INTEL_ONE, None],
    },
    29: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, None, A.INTEL_ONE],
    },
    30: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.SOCIAL_ONE, None, A.CREATE_ONE],
    },
    31: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, None, A.SOCIAL_ONE],
    },
    32: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.INTEL_ONE, None, A.CREATE_ONE],
    },
    33: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, None, A.SOCIAL_ONE],
    },
    34: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [A.CREATE_ONE, None, A.INTEL_ONE],
    },
    35: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.SOCIAL_ONE, A.INTEL_ONE],
    },
    36: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.SOCIAL_ONE, A.CREATE_ONE],
    },
    37: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.INTEL_ONE, A.SOCIAL_ONE],
    },
    38: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.INTEL_ONE, A.CREATE_ONE],
    },
    39: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.CREATE_ONE, A.SOCIAL_ONE],
    },
    40: {
        "board_slot": B.BOARD_SLOT_ONE,
        "values": [None, A.CREATE_ONE, A.INTEL_ONE],
    },
    41: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, A.CONST_ONE, None],
    },
    42: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, A.COORD_ONE, None],
    },
    43: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, A.STRENGTH_ONE, None],
    },
    44: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, A.COORD_ONE, None],
    },
    45: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, A.STRENGTH_ONE, None],
    },
    46: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, A.CONST_ONE, None],
    },
    47: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, None, A.CONST_ONE],
    },
    48: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.STRENGTH_ONE, None, A.COORD_ONE],
    },
    49: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, None, A.STRENGTH_ONE],
    },
    50: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.CONST_ONE, None, A.COORD_ONE],
    },
    51: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, None, A.STRENGTH_ONE],
    },
    52: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [A.COORD_ONE, None, A.CONST_ONE],
    },
    53: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.STRENGTH_ONE, A.CONST_ONE],
    },
    54: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.STRENGTH_ONE, A.COORD_ONE],
    },
    55: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.CONST_ONE, A.STRENGTH_ONE],
    },
    56: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.CONST_ONE, A.COORD_ONE],
    },
    57: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.COORD_ONE, A.STRENGTH_ONE],
    },
    58: {
        "board_slot": B.BOARD_SLOT_TWO,
        "values": [None, A.COORD_ONE, A.CONST_ONE],
    },
    59: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.DETERM_ONE, A.EMPATHY_ONE, None],
    },
    60: {
        "board_slot": B.BOARD_SLOT_THREE,
        "values": [A.EMPATHY_ONE, A.DETERM_ONE, None],
    },
    61: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_THREE, None, None],
    },
    62: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_THREE, None, None],
    },
    63: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_THREE, None, None],
    },
    64: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.SOCIAL_THREE, None],
    },
    65: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.INTEL_THREE, None],
    },
    66: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.CREATE_THREE, None],
    },
    67: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, None, A.SOCIAL_THREE],
    },
    68: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, None, A.INTEL_THREE],
    },
    69: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, None, A.CREATE_THREE],
    },
    70: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_THREE, None, None],
    },
    71: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_THREE, None, None],
    },
    72: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_THREE, None, None],
    },
    73: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.STRENGTH_THREE, None],
    },
    74: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.CONST_THREE, None],
    },
    75: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.COORD_THREE, None],
    },
    76: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, None, A.STRENGTH_THREE],
    },
    77: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, None, A.CONST_THREE],
    },
    78: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, None, A.COORD_THREE],
    },
    79: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.EMPATHY_THREE, None, None],
    },
    80: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.DETERM_THREE, None, None],
    },
    81: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [None, A.EMPATHY_THREE, None],
    },
    82: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [None, A.DETERM_THREE, None],
    },
    83: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, A.INTEL_TWO, None],
    },
    84: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, A.CREATE_TWO, None],
    },
    85: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, A.SOCIAL_TWO, None],
    },
    86: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, A.CREATE_TWO, None],
    },
    87: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, A.SOCIAL_TWO, None],
    },
    88: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, A.INTEL_TWO, None],
    },
    89: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, None, A.INTEL_TWO],
    },
    90: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.SOCIAL_TWO, None, A.CREATE_TWO],
    },
    91: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, None, A.SOCIAL_TWO],
    },
    92: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.INTEL_TWO, None, A.CREATE_TWO],
    },
    93: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, None, A.SOCIAL_TWO],
    },
    94: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [A.CREATE_TWO, None, A.INTEL_TWO],
    },
    95: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.SOCIAL_TWO, A.INTEL_TWO],
    },
    96: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.SOCIAL_TWO, A.CREATE_TWO],
    },
    97: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.INTEL_TWO, A.SOCIAL_TWO],
    },
    98: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.INTEL_TWO, A.CREATE_TWO],
    },
    99: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.CREATE_TWO, A.SOCIAL_TWO],
    },
    100: {
        "board_slot": B.BOARD_SLOT_FOUR,
        "values": [None, A.CREATE_TWO, A.INTEL_TWO],
    },
    101: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, A.CONST_TWO, None],
    },
    102: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, A.COORD_TWO, None],
    },
    103: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, A.STRENGTH_TWO, None],
    },
    104: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, A.COORD_TWO, None],
    },
    105: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, A.STRENGTH_TWO, None],
    },
    106: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, A.CONST_TWO, None],
    },
    107: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, None, A.CONST_TWO],
    },
    108: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.STRENGTH_TWO, None, A.COORD_TWO],
    },
    109: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, None, A.STRENGTH_TWO],
    },
    110: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.CONST_TWO, None, A.COORD_TWO],
    },
    111: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, None, A.STRENGTH_TWO],
    },
    112: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [A.COORD_TWO, None, A.CONST_TWO],
    },
    113: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.STRENGTH_TWO, A.CONST_TWO],
    },
    114: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.STRENGTH_TWO, A.COORD_TWO],
    },
    115: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.CONST_TWO, A.STRENGTH_TWO],
    },
    116: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.CONST_TWO, A.COORD_TWO],
    },
    117: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.COORD_TWO, A.STRENGTH_TWO],
    },
    118: {
        "board_slot": B.BOARD_SLOT_FIVE,
        "values": [None, A.COORD_TWO, A.CONST_TWO],
    },
    119: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.DETERM_TWO, A.EMPATHY_TWO, None],
    },
    120: {
        "board_slot": B.BOARD_SLOT_SIX,
        "values": [A.EMPATHY_TWO, A.DETERM_TWO, None],
    },
    121: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_FOUR, None, None],
    },
    122: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_FOUR, None, None],
    },
    123: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_FOUR, None, None],
    },
    124: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.SOCIAL_FOUR, None],
    },
    125: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.INTEL_FOUR, None],
    },
    126: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.CREATE_FOUR, None],
    },
    127: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, None, A.SOCIAL_FOUR],
    },
    128: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, None, A.INTEL_FOUR],
    },
    129: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, None, A.CREATE_FOUR],
    },
    130: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_FOUR, None, None],
    },
    131: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_FOUR, None, None],
    },
    132: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_FOUR, None, None],
    },
    133: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.STRENGTH_FOUR, None],
    },
    134: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.CONST_FOUR, None],
    },
    135: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.COORD_FOUR, None],
    },
    136: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, None, A.STRENGTH_FOUR],
    },
    137: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, None, A.CONST_FOUR],
    },
    138: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, None, A.COORD_FOUR],
    },
    139: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.EMPATHY_FOUR, None, None],
    },
    140: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.DETERM_FOUR, None, None],
    },
    141: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [None, A.EMPATHY_FOUR, None],
    },
    142: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [None, A.DETERM_FOUR, None],
    },
    143: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, A.INTEL_TWO, None],
    },
    144: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, A.CREATE_TWO, None],
    },
    145: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, A.SOCIAL_TWO, None],
    },
    146: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, A.CREATE_TWO, None],
    },
    147: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, A.SOCIAL_TWO, None],
    },
    148: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, A.INTEL_TWO, None],
    },
    149: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, None, A.INTEL_TWO],
    },
    150: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.SOCIAL_TWO, None, A.CREATE_TWO],
    },
    151: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, None, A.SOCIAL_TWO],
    },
    152: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.INTEL_TWO, None, A.CREATE_TWO],
    },
    153: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, None, A.SOCIAL_TWO],
    },
    154: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [A.CREATE_TWO, None, A.INTEL_TWO],
    },
    155: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.SOCIAL_TWO, A.INTEL_TWO],
    },
    156: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.SOCIAL_TWO, A.CREATE_TWO],
    },
    157: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.INTEL_TWO, A.SOCIAL_TWO],
    },
    158: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.INTEL_TWO, A.CREATE_TWO],
    },
    159: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.CREATE_TWO, A.SOCIAL_TWO],
    },
    160: {
        "board_slot": B.BOARD_SLOT_SEVEN,
        "values": [None, A.CREATE_TWO, A.INTEL_TWO],
    },
    161: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, A.CONST_TWO, None],
    },
    162: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, A.COORD_TWO, None],
    },
    163: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, A.STRENGTH_TWO, None],
    },
    164: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, A.COORD_TWO, None],
    },
    165: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, A.STRENGTH_TWO, None],
    },
    166: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, A.CONST_TWO, None],
    },
    167: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, None, A.CONST_TWO],
    },
    168: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.STRENGTH_TWO, None, A.COORD_TWO],
    },
    169: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, None, A.STRENGTH_TWO],
    },
    170: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.CONST_TWO, None, A.COORD_TWO],
    },
    171: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, None, A.STRENGTH_TWO],
    },
    172: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [A.COORD_TWO, None, A.CONST_TWO],
    },
    173: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.STRENGTH_TWO, A.CONST_TWO],
    },
    174: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.STRENGTH_TWO, A.COORD_TWO],
    },
    175: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.CONST_TWO, A.STRENGTH_TWO],
    },
    176: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.CONST_TWO, A.COORD_TWO],
    },
    177: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.COORD_TWO, A.STRENGTH_TWO],
    },
    178: {
        "board_slot": B.BOARD_SLOT_EIGHT,
        "values": [None, A.COORD_TWO, A.CONST_TWO],
    },
    179: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.DETERM_TWO, A.EMPATHY_TWO, None],
    },
    180: {
        "board_slot": B.BOARD_SLOT_NINE,
        "values": [A.EMPATHY_TWO, A.DETERM_TWO, None],
    },
}
