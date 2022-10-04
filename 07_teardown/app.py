# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. I've seen it in javascript and java.
1. '/' is the home route/directory.
2. This prints to the title of the homepage.
3. It prints __main__ which is "127.0.0.1:5000".
4. It appears as the body of the website. I click link and saw.
5. I've seen this a lot in java for calling methods in a class.
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
