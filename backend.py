from flask import Flask, render_template, request, redirect
import random
import time
import main
import WSBSentimentAnalyzer

app = Flask(__name__)

analyzer = WSBSentimentAnalyzer.SentimentAnalyzer()
parser = WSBSentimentAnalyzer.RedditDataParser()
#data = parser.getRedditData('wsb-sample.csv', 80000)
#parsed_data = parser.parseData(data)

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def dashboard():



    data = {}
    tickers = ['NDX','GME','AAPL','SPY']
    stock_data = main.getStockData(tickers, "1mo", "1d")


    for i,d in enumerate(stock_data):
        data[d['name']] = {}
        data[d['name']]['prices'] = d['data']
        data[d['name']]['sentiments'] = [(time.time()-random.randint(0,10), random.uniform(-1, 1)) for i in range(50)]

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
