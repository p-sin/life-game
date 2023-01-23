from life_game.setup.event_cards import event_type, condition_type
from life_game.setup.components import Board


def single_total(board: Board, condition: condition_type) -> bool:
    return getattr(board, condition["attribute"]) == condition["value"]


def min_total(board: Board, condition: condition_type) -> bool:
    total_value = 0

    for attribute in condition["attributes"]:
        if getattr(board, attribute) >= 1:
            total_value += getattr(board, attribute)
        else:
            return False

    return total_value >= 4


def max_value(board: Board, condition: condition_type) -> bool:
    final_max = 0

    for attribute in [
        "Sociability",
        "Intelligence",
        "Creativity",
        "Strength",
        "Constitution",
        "Coordination",
        "Empathy",
        "Determination",
    ]:
        if getattr(board, attribute) > final_max:
            final_max = getattr(board, attribute)

    return final_max <= condition["max_value"]


event_map = {
    "single_total": single_total,
    "min_total": min_total,
    "max_value": max_value,
}


def resolve_event(board: Board, event: event_type) -> int:
    final_points = 0

    for _, outcome in event["outcomes"].items():
        if event_map[outcome["type"]](board, outcome["condition"]):
            if outcome["points"] > final_points:
                final_points = outcome["points"]

    return final_points
