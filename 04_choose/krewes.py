"""
Chicken Fries (Mahir Riki, Vivian Teo, Gabriel Thompson)
SoftDev
K04 -- python file that randomly generates a devopler
2022-09-22
time spent: 0.3 hours
"""
krewes = {2:["a2","b2","c2"], 7:["a7","b7","c7"], 8:["a8","b8","c8"]}

import random
def randomDevo(krewes):
    return random.choice(random.choice(list(krewes.values())))

print(randomDevo(krewes))
