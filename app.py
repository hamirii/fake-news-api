from flask import Flask
import json


app = Flask(__name__)

# There is a much better way of doing this - compiling everything into one Json file with the appropriate tag (i.e. "sports")


@ app.route('/')
def home():
    return "Fake News API Service"


@ app.route('/latest', methods=['GET'])
def latest():
    with open('articlesLibrary/latestArticles.json') as f:
        apiLatest = json.load(f)
    return apiLatest


@ app.route('/apiLib')
def apiLib():
    with open('articlesLibrary/articlesAPI.json') as f:
        apiLib = json.load(f)
    return apiLib


'''
@ app.route('/sports', methods=['GET'])
def sports():
    with open('articlesLibrary/sportsArticles.json') as f:
        apiLatest = json.load(f)
    return apiLatest


@ app.route('/politics', methods=['GET'])
def politics():
    with open('articlesLibrary/politicsArticles.json') as f:
        apiPolitics = json.load(f)
    return apiPolitics


@ app.route('/film', methods=['GET'])
def film():
    with open('articlesLibrary/filmArticles.json') as f:
        apiFilm = json.load(f)
    return apiFilm


@ app.route('/tech', methods=['GET'])
def tech():
    with open('articlesLibrary/techArticles.json') as f:
        apiTech = json.load(f)
    return apiTech
'''

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
