from typing import Dict, List, Union

ConditionType = Dict[str, Union[str, int, List[str]]]
OutcomeType = Dict[str, Union[str, int, ConditionType]]
event_type = Dict[str, Union[str, Dict[str, OutcomeType]]]
event_cards: Dict[int, event_type] = {
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
                    "attribute": "Coordination",
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
    2: {
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
                    "attribute": "Strength",
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
    3: {
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
                    "attribute": ["Coordination", "Determination"],
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
                    "attribute": "Intelligence",
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
                    "attribute": ["Strength", "Constitution"],
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
                    "attribute": ["Creativity", "Empathy"],
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
                    "attribute": "Creativity",
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
                    "attribute": ["Sociability", "Empathy"],
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
    8: {
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
                    "attribute": "Constitution",
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
    9: {
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
                    "attribute": "Empathy",
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
    10: {
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
                    "attribute": ["Coordination", "Strength"],
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
                    "attribute": "Sociability",
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
                    "attribute": ["Creativity", "Constitution"],
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
                    "attribute": ["Intelligence", "Empathy"],
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
    14: {
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
                    "attribute": ["Coordination", "Constitution"],
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
                    "attribute": "Sociability",
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
                    "attribute": ["Constitution", "Empathy"],
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
                    "attribute": ["Intelligence", "Creativity"],
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
                    "attribute": "Strength",
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
                    "attribute": ["Intelligence", "Sociability"],
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
                    "attribute": ["Creativity", "Sociability"],
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
                    "attribute": "Determination",
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
    20: {
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
                    "attribute": ["Creativity", "Coordination"],
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
                    "attribute": "Determination",
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
    22: {
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
                    "attribute": "Creativity",
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
    23: {
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
                    "attribute": "Strength",
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
    24: {
        "flav_text": "",
        "life_stage": "child",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 1,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
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
                    "attribute": ["Intelligence", "Coordination"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    25: {
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
                    "attribute": "Sociability",
                    "value": 2,
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
    26: {
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
                    "attribute": "Constitution",
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
    27: {
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
                    "attribute": "Sociability",
                    "value": 2,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Empathy"],
                    "total": 4,
                    "min": 1,
                },
            },
        },
    },
    28: {
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
                    "attribute": ["Determination", "Empathy"],
                    "total": 4,
                    "min": 1,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Coordination"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Constitution"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Empathy"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Empathy"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Determination"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Determination"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Constitution"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Strength"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Constitution"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Strength"],
                    "total": 7,
                    "min": 3,
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
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Constitution"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    43: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Empathy"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    44: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Creativity"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    45: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Sociability"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    46: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Sociability"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    47: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    48: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Coordination"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    49: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Strength"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    50: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Determination"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    51: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Constitution"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    52: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Coordination"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    53: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    54: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Strength"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    55: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Empathy"],
                    "total": 7,
                    "min": 3,
                },
            },
        },
    },
    56: {
        "flav_text": "",
        "life_stage": "adol",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 5,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 3,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 5,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 3,
                "type": "min",
                "condition": {
                    "attribute": ["Determination", "Empathy"],
                    "total": 7,
                    "min": 3,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Determination"],
                    "total": 10,
                    "min": 6,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Coordination"],
                    "total": 10,
                    "min": 6,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 10,
                    "min": 6,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Constitution"],
                    "total": 10,
                    "min": 6,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Empathy"],
                    "total": 10,
                    "min": 6,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Empathy"],
                    "total": 10,
                    "min": 6,
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
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Determination"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    64: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Determination"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    65: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Constitution"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    66: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Strength"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    67: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Constitution"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    68: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    69: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Strength"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    70: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Constitution"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    71: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Empathy"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    72: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Creativity"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    73: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Sociability"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    74: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Sociability"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    75: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Empathy"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    76: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Coordination"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    77: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Strength"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    78: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Constitution", "Determination"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    79: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Sociability", "Constitution"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    80: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Empathy",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Determination",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Intelligence", "Coordination"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    81: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Intelligence",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Coordination", "Determination"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    82: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Coordination",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Creativity", "Strength"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    83: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Creativity",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Sociability",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Strength", "Empathy"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
    84: {
        "flav_text": "",
        "life_stage": "adult",
        "outcomes": {
            "outcome_1": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Strength",
                    "value": 8,
                },
            },
            "outcome_2": {
                "flav_text": "",
                "points": 5,
                "type": "single",
                "condition": {
                    "attribute": "Constitution",
                    "value": 8,
                },
            },
            "outcome_3": {
                "flav_text": "",
                "points": 5,
                "type": "min",
                "condition": {
                    "attribute": ["Determination", "Empathy"],
                    "total": 10,
                    "min": 6,
                },
            },
        },
    },
}
