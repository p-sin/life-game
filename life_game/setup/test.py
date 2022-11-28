from cards import cards
from definitions import BoardSlots as B

test_dict = {}

for key, dict in cards.items():
    if dict["board_slot"].value.number not in test_dict.keys():
        test_dict[dict["board_slot"].value.number] = 0
    test_dict[dict["board_slot"].value.number] += 1

    if 

print (test_dict)
