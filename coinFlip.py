from random import random

def flip_coin():
    if random() > 0.5:
        return "heads"
    else:
        return "tails"

print(flip_coin())