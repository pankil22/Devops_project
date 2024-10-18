from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

# List of RSS feed URLs from different news sources
RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'nyt': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'jagran_hindi': 'https://rss.jagran.com/rss/news/national.xml',  # Jagran Hindi
}




def get_news(source='bbc'):
    # Fetching news from the selected RSS feed
    feed = feedparser.parse(RSS_FEEDS.get(source, RSS_FEEDS['bbc']))
    return feed.entries

@app.route('/')
def index():
    source = request.args.get('source', 'bbc')
    articles = get_news(source)
    return render_template('index.html', articles=articles, source=source)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
