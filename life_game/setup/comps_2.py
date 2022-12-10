from setup.cards import card_type
from typing import Optional

hand_type = dict[str, Optional[card_type]]

base_hand: hand_type = {
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "7": None,
    "8": None,
    "9": None,
}