from dataclasses import dataclass

@dataclass
class Board:
    """Defines the playerboard"""
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

@dataclass
class PlayerBoard(Board):
    player: int
    sociability: int
    intelligence: int
    creativity: int	
    strength: int
    constitution: int
    coordination: int
    empathy: int
    determination: int