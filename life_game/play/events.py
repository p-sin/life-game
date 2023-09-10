from life_game.components.components import Board
from life_game.components.event_cards import condition_type, event_type


def single_total(board: Board, condition: condition_type) -> bool:
    return getattr(board, condition["attribute"]) >= condition["value"]  # type: ignore


def min_total(board: Board, condition: condition_type) -> bool:
    total_value = 0

    for attribute in condition["attribute"]:  # type: ignore
        if getattr(board, attribute) >= condition["min"]:
            total_value += getattr(board, attribute)
        else:
            return False

    return total_value >= condition["total"]  # type: ignore


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

    return final_max <= condition["max_value"]  # type: ignore


event_map = {
    "single_total": single_total,
    "min_total": min_total,
    "max_value": max_value,
}


def resolve_event(board: Board, event: event_type) -> int:
    final_points = 0

    for _, outcome in event["outcomes"].items():  # type: ignore
        if event_map[outcome["type"]](board, outcome["condition"]):  # type: ignore
            if outcome["points"] > final_points:  # type: ignore
                final_points = outcome["points"]  # type: ignore

    return final_points
