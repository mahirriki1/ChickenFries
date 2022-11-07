# WeLoveTrees - Mahir Riki, Ravindra Mangar, Kevin Liu
# SoftDev
# K19: Sessions Greetings
# 2022-11-03
# time spent: 0.5 hr

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = '1a674c5cf44a5aa2eb768cb976ca141ccc2abe287877eab90649ec94f4974b11'

username = "WeLoveTrees"
password = "trees"

@app.route("/")
def login():
    if 'username' in session:
        return render_template('response.html')
    return render_template('login.html')

@app.route('/response', methods=['GET', 'POST'])
def response():
    if request.method == 'POST':
        usr = request.form['username']
        passw = request.form['password']
    if username in usr and password in passw:
        session['username'] = request.form['username']
        print(session)
        return render_template('response.html')
    # for blank responses
    if "" == usr and "" in passw:
        return "Enter a username and password." + render_template('login.html')
    elif "" == usr or "" == passw:
        return "Username or password is blank." + render_template('login.html')
    # for incorrect username/password
    if usr != username or passw != password:
        return "Username or password is incorrect." + render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None) # remove username from session
    return '<p>You have been logged out</p>'+ '\n\n' + render_template('login.html')

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run() 