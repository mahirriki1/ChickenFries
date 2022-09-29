import random
from tkinter import N


with open('krewes.txt', 'r') as f:
    lines = f.readline()
krewes_list = lines.split("@@@")

krewes = {2: [],
          7: [],
          8: []
          }
          
for i in krewes_list:
    person = i.split("$$$")
    if (not int(person[0]) in krewes.keys()):
        krewes[int(person[0])] = []
    list = [person[1], person[2]]
    krewes[int(person[0])].append(list)

def random_devo(krewes):
# printing both the devo's name, period, and ducky
    period = random.choice(krewes.keys())
    person_and_ducky = random.choice(list(krewes[period]))
    name = person_and_ducky[0]
    ducky = person_and_ducky[1]
    print(period + ", " + name + ", " + ducky)
    
print(random_devo(krewes))
