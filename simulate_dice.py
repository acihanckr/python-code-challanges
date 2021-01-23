from collections import defaultdict
from random import randint
import random

def simulate_dice(*args):
    dice = list(args)
    outcomes = defaultdict(int)
    for i in range(100000000):
        result = sum([randint(1, die) for die in dice])
        outcomes[result] += 1
    total = sum(outcomes.values())
    probabilities = {k:v/total for k,v in outcomes.items()} 
    return probabilities


random.seed(314)
simulation = simulate_dice(4,6,6)
for k in sorted(simulation.keys()):
    print(f'{k}: {round(simulation[k]*100,2)}%')
