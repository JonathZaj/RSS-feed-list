import feedparser
import json
from bottle import route, run, template
import ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


feed = feedparser.parse('https://www.dailymail.co.uk/articles.rss')



@route('/')
def app():
    return template("index.html")


@route('/links')
def headline():
    headlines = []
    for i in range(len(feed["entries"])):
        text = "<a href={0}>{1}</a>".format(feed['entries'][i]["link"], feed["entries"][i]["title"])
        headlines.append(text)
    return json.dumps(headlines)


def main():
    run(host='localhost', port=7001)


if __name__ == '__main__':
    main()
