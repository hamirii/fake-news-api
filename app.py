from flask import Flask
import json


app = Flask(__name__)


@ app.route('/')
def home():
    return "Fake News API Service"


@ app.route('/apiLib')
def apiLib():
    with open('articlesLibrary/articlesAPI.json') as f:
        apiLib = json.load(f)
    return apiLib


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
