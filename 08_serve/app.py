""" 
MyJuicyWork - Mahir Riki, Jacob Guo, William Guo
SoftDev
K08 -- serve
2022-10-06
time spent: 
"""
"""
Plan:
- Copy numbercruncher code to this file.
-
"""

import random as r
from flask import Flask

# used to split up each occupation with commmas in their name
def specialSplit(string):
    splitted = []
    lastIndex = 0
    locked = False
    for i in range(len(string)):
        theChar = string[i]
        if (theChar == "\""):
            locked = not locked
        if (theChar == "," and (not locked)):
            splitted.append(string[lastIndex: i])
            lastIndex = i+1
    splitted.append(string[lastIndex:-1])
    return splitted

reading = open("occupations.csv", "r") # opens "occupations.csv" and just reads it
list_of_all_text = reading.readlines() # turns each line of the csv file into a list 

# this makes another list that splits up the occupations correctly by ,
parsed_text = []
for i in list_of_all_text:
    parsed_text.append(specialSplit(i))

# to make the occupations dictionary
occupations = {}
for i in range(len(parsed_text)):
    job = parsed_text[i]
    if (i == 0):
        occupations[job[0]] = job[1]
    else:
        occupations[job[0]] = float(job[1])
occupations.pop('Job Class') # removes the job class key from the dictionary
occupations.pop('Total') # removes the total key from the dictionary

# function for weighted randomly selected occupations
def occupation_selector():
    percentages = list(occupations.values())
    occupation = r.choices(list(occupations.keys()), weights = percentages)
    return occupation[0]

app = Flask(__name__)

@app.route("/")
def random_occupation():
    print(__name__)
    return occupation_selector() + "<br>" + "<br>" + str(occupations.keys())

app.debug = True
app.run()
