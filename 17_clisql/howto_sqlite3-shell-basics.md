# Team WeLoveTrees - Kevin Liu, Ravindra Mangar, Mahir Riki
## K17: Shell Game
## SoftDev
## 24-10-2022
## Time Spent: ~30 minutes

---

## Table of Contents
- [0. How To RUN SQLITE in Terminal](#0)
- [1. Creating a New Table](#1)

---

<br>

### <a id = 0> </a> 0. How to Run SQLITE in Terminal
<br>
Open a new terminal and type ```sqlite3 <DATABASE NAME>```.<b> REMEMBER THE "3".</b>

<br>

### <a id = 1> </a> 1. Creating a New Table

<br>

To create a new table, type ```CREATE TABLE <TABLE NAME>(<COLUMN NAME> <DATA TYPE>);```. <br>
* For example, to create a table called "students" with a column called "name" that stores strings, type ```CREATE TABLE students(name TEXT);```.

To insert into this table, you type ```INSERT INTO <TABLE NAME> VALUES(<VALUE>);```. <br>
* For example, to insert "Qiu Qiu Kachu" into the "students" table, type ```INSERT INTO students VALUES("Qiu Qiu Kachu");```.

To view the table, type ```SELECT * FROM <TABLE NAME>;```. <br>
* For example, to view the "students" table, type ```SELECT * FROM students;```.