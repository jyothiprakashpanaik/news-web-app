import requests
from flask import Flask, render_template
from newsapi import NewsApiClient
import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=4659d4fbf33e45edade3b21f0e19899a')
app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get(url)
    articles = response.json()['articles']
    news = []
    desc = []
    images = []
    links = []

    for i in range(len(articles)):
        myarticle = articles[i]

        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        images.append(myarticle['urlToImage'])
        links.append(myarticle['url'])

    myList = zip(news, desc, images, links)

    return render_template('index.html',context=myList)
    

@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key='4659d4fbf33e45edade3b21f0e19899a')
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    news = []
    desc = []
    images = []
    links = []

    for i in range(len(articles)):
        myarticle = articles[i]

        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        images.append(myarticle['urlToImage'])
        links.append(myarticle['url'])

    myList = zip(news, desc, images, links)

    return render_template('index.html',context=myList)
    



if __name__ == "__main__":
	app.run(debug=True)