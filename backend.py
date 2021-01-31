from flask import Flask, render_template, request, redirect, jsonify
import random
import time
import main

app = Flask(__name__)


# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def dashboard():
    data = {}
    tickers = ['NDX', 'GME', 'AAPL', 'SPY']
    stock_data = main.getStockData(tickers, "1mo", "1d")
    for i, d in enumerate(stock_data):
        data[d['name']] = {}
        data[d['name']]['prices'] = d['data']
        data[d['name']]['sentiments'] = [
            (time.time()-random.randint(0, 10), random.uniform(-1, 1)) for i in range(50)]

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
