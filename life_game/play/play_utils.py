from typing import Tuple

# Temp object to hold the calculated attribute totals for each player.
# To then be set as the actual values in the player's board object
attribute_total_calc: dict[str, int] = {
    "Sociability": 0,
    "Intelligence": 0,
    "Creativity": 0,
    "Strength": 0,
    "Constitution": 0,
    "Coordination": 0,
    "Empathy": 0,
    "Determination": 0,
}


def card_num_start_end(player_num: int) -> Tuple[int, int]:
    start = 0 + (9 * (player_num - 1))
    end = 9 + (9 * (player_num - 1))
    return start, end
