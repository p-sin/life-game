from setup.players import Board, hand_type, card_type
from setup.components import Attributes
import random
from typing import Tuple

def select_card(hand: hand_type) -> list[int]:

    hand_list = list(hand.keys())

    return random.sample(hand_list, 2)

def card_slot_info(card: card_type, slot: int) -> Tuple[int, Attributes]:
    slot_num = card["card_slot_" + str(slot)]["slot_number"]
    slot_value = card["card_slot_" + str(slot)]["values"]

    return slot_num, slot_value

def play_card(board: Board, hand: hand_type, card: int) -> Board:

    card = hand[card]

    for slot in range (1,4):
        slot_num, slot_value = card_slot_info(card, slot)

        if slot_num != None:
            board.attribute_slots[slot_num]["type"] = slot_value.name
            board.attribute_slots[slot_num]["value"] = slot_value.value

    return board

    
    

