"""
Chicken Fries (Mahir Riki, Vivian Teo, Gabriel Thompson)
SoftDev
K04 -- krewes
2022-09-22
time spent: 0.5 hours

OPS: Randomly generates a developer and their period from a dictionary in dictionary.py. The
keys in the dictionary are periods, and each key has a value of lists with developer names. The
program first randomly selects a key from the dictionary using random.choice, then randomly selects
a name from the list corresponding with that period using random.choice. Finally, the program
prints out both.
"""

import dictionary
import random

def randomDevo(krewes):
# printing only the devo's name
    # print(random.choice(random.choice(list(krewes.values()))))
# printing both the devo's name and period
    key = random.choice(list(dict.keys(krewes)))
    name = random.choice(list(krewes[key]))
    print(str(key)+", "+name)
    
(randomDevo(dictionary.krewes))
