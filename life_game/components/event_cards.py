from typing import Union

condition_type = dict[str, Union[Union[str, int], list[str]]]
outcome_type = dict[str, dict[str, Union[str, int, condition_type]]]
event_type = dict[str, Union[str, outcome_type]]
event_cards: dict[int, event_type] = {
    1: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Strength"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    2: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Constitution"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    3: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Coordination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    4: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Empathy"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    5: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    6: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Strength"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    7: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Constitution"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    8: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Coordination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    9: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    10: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    11: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Strength"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    12: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Constitution"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    13: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Coordination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    14: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Empathy"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    15: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    16: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    17: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    18: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Empathy"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    19: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    20: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Empathy"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    21: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "max",
                "condition": {
                    "max_value": 2,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 1,
                "type": "max",
                "condition": {
                    "max_value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    22: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Strength"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    23: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Constitution"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    24: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Coordination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    25: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Empathy"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    26: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    27: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Strength"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    28: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Constitution"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    29: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Coordination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    30: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    31: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    32: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Strength"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    33: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Constitution"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    34: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Coordination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    35: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Empathy"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    36: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    37: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    38: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    39: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Empathy"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    40: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    41: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Empathy"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    42: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 4,
                "type": "max",
                "condition": {
                    "max_value": 4,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 4,
                "type": "max",
                "condition": {
                    "max_value": 4,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 8,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 8,
                    "min": 2,
                },
            },
        },
    },
    43: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Strength"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    44: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Constitution"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    45: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Coordination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    46: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Empathy"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    47: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    48: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Strength"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    49: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Constitution"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    50: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Coordination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    51: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    52: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    53: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Strength"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    54: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Constitution"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    55: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Coordination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    56: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Empathy"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    57: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    58: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    59: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    60: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Empathy"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    61: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    62: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Empathy"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
    63: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 6,
                "type": "max",
                "condition": {
                    "max_value": 6,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 6,
                "type": "max",
                "condition": {
                    "max_value": 6,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 15,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 12,
                    "min": 4,
                },
            },
        },
    },
}
