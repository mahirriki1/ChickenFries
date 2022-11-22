from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main():
    # to get key from key_nasa.txt
    f = open('key_nasa.txt', 'r')
    key = f.read()
    
    # using the nasa api
    url = f"https://api.nasa.gov/planetary/apod?api_key={key}";
    content = requests.get(url).json()
    
    return render_template('main.html', title = content.get('title'), img_url = content.get('url'), explanation = content.get('explanation'))

if __name__ == '__main__':
    app.run(debug=True)