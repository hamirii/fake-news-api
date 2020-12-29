from flask import Flask
from flask import jsonify

apiLib = [{"url": "https://github.com/",
          "imageURL": 'hi',
          "logo": 'hi',
          "headline": 'Headlines22'},
          {"url": "https://google.com/",
          "imageURL": "hello",
          "logo": "hoo",
          "headline": "What's up?"}

app= Flask(__name__)


@ app.route('/')
def home():
    return "Fake News API Service"


@ app.route('/sports', methods=['GET'])
def sport():
    return apiLib


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
