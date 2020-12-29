from flask import Flask

apiLib = {"articles": [

    {
        "headline": "Arsenal to win Premier League in shock Arsene Wenger comeback",
        'imageURI': 'https://cdn.newsapi.com.au/image/v1/5ce735885933ff71f6943eb9b4b68c1c',
        'imageLogo': 'https://i.ibb.co/5rBMVXF/BBC-logo.png',
        'url': "https://www.bbc.com/sport/football/55382725"},

    {
        "headline": "Whole Foods wins Nobel Prize for solving Climate Change with $60 Dijon Mustard products",
        "imageURI": "https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/content/15/e7/47c9886840b299bd24b6e48fca6e/7.Certified-Organic-Grocery-Store_2280x1282._TTW_._CR1,0,2278,1282_._SR1500,844_._QL100_.jpg",
        "imageLogo": 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/CNN.svg/900px-CNN.svg.png'
    },

    {
        "headline": "Fish Fingers, as it turns out, are not made from real fish",
        "imageURI": 'https://www.irishtimes.com/polopoly_fs/1.3696142.1542101165!/image/image.jpg',
        "imageLogo": 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/CTV_logo_2018.svg/1200px-CTV_logo_2018.svg.png'
    }

]}

app = Flask(__name__)


@ app.route('/')
def home():
    return "Fake News API Service"


@ app.route('/latest', methods=['GET'])
def latest():
    return apiLib


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
