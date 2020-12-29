from flask import Flask
import json

apiLib = {"url": "https://github.com/", "imageURL": 'hi',
          "logo": 'hi', "headline": 'Headline'}

app = Flask(__name__)


@app.route('/')
def home():
    return "Fake News API Service"


@app.route('/sports', methods=['GET'])
def sport():
    return apiLib


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
