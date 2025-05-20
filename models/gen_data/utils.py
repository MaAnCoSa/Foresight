import random

def roll_d20(advantage=False, disadvantage=False):
    return {
        "rolls": [random.randint(1, 20), random.randint(1, 20)],
        "advantage": advantage,
        "disadvantage": disadvantage,
        "modifiers": 0
    }
