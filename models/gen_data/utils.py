import random

def roll_d20(advantage=False, disadvantage=False):
    # Rolls a d20 and returns the result. If advantage is True, rolls two d20s and returns the higher result.
    if advantage:
        return max(random.randint(1, 20), random.randint(1, 20))
    elif disadvantage:
        return min(random.randint(1, 20), random.randint(1, 20))
    else:
        return random.randint(1, 20)