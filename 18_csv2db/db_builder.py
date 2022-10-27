# WeLoveTrees -- Mahir Riki, Ravindra Mangar, Kevin Liu
# SoftDev
# K18: (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-25
# time spent: 2 hrs

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

coursesDict = csv.DictReader(open("courses.csv"))
studentsDict = csv.DictReader(open("students.csv"))

#==========================================================

c.execute("CREATE TABLE IF NOT EXISTS courses(code, mark, id)") # run SQL query
c.execute("CREATE TABLE IF NOT EXISTS students(name, age, id)")

for row in coursesDict:
    row_dict = dict(row)
    c.execute("INSERT INTO courses VALUES(?, ?, ?)", (row_dict["code"], row_dict["mark"], row_dict["id"]))
    
for row in studentsDict:
    row_dict = dict(row)
    c.execute("INSERT INTO students VALUES(?, ?, ?)", (row_dict["name"], row_dict["age"], row_dict["id"]))

#==========================================================

#VERIFICATION
#c.execute("SELECT * FROM courses")
#print(c.fetchall()) #prints all rows in courses table
#c.execute("SELECT * FROM students")
#print(c.fetchall()) #prints all rows in students table

db.commit() #save changes
db.close()  #close database