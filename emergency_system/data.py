graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 7, "E": 3},
    "C": {"A": 4, "F": 5},
    "D": {"B": 7},
    "E": {"B": 3, "F": 1},
    "F": {"C": 5, "E": 1}
}

heuristic = {
    "A": 7, "B": 6, "C": 2,
    "D": 1, "E": 1, "F": 0
}

services = {
    "Fire": "D",
    "Medical": "F",
    "Police": "E"
}
