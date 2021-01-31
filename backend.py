from flask import Flask, render_template, request, redirect, jsonify
import random
import time
import WSBSentimentAnalyzer
import analytics_tools
from PostSentimentMaintainer import getSentimentData

app = Flask(__name__)


# Create some test data for our catalog in the form of a list of dictionaries.

@app.route('/api/v1/financialData', methods=['GET'])
def handleGetFinancialData():
    ticker = ''
    period = ''
    interval = ''

    if 'ticker' in request.args:
        ticker = str(request.args['ticker'])
    else:
        return "Error: No ticker field provided. Please specify a ticker."

    if 'period' in request.args:
        period = str(request.args['period'])
        print(period)
    else:
        return "Error: No period field provided. Please specify a period."

    if 'interval' in request.args:
        interval = str(request.args['interval'])
    else:
        return "Error: No interval field provided. Please specify a interval."

    stonks = analytics_tools.getStockData([ticker], period, interval)

    return jsonify({'data': stonks})


@app.route('/api/v1/sentimentData', methods=['GET'])
def handleGetSentimentData():
    ticker = ''
    period = ''
    interval = ''

    if 'ticker' in request.args:
        ticker = str(request.args['ticker'])
    else:
        return "Error: No ticker field provided. Please specify a ticker."

    if 'period' in request.args:
        period = str(request.args['period'])
        print(period)
    else:
        return "Error: No period field provided. Please specify a period."

    if 'interval' in request.args:
        interval = str(request.args['interval'])
    else:
        return "Error: No interval field provided. Please specify a interval."

    sentis = getSentimentData([ticker], period, interval)

    return jsonify({'data': sentis})


analyzer = WSBSentimentAnalyzer.SentimentAnalyzer()
parser = WSBSentimentAnalyzer.RedditDataParser()
# data = parser.getRedditData('wsb-sample.csv', 80000)
# parsed_data = parser.parseData(data)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def dashboard():

    data = {}
    tickers = ['NDX', 'GME', 'AAPL', 'SPY']
    stock_data = analytics_tools.getStockData(tickers, "1mo", "1d")

    for i, d in enumerate(stock_data):
        data[d['name']] = {}
        data[d['name']]['prices'] = d['data']
        data[d['name']]['sentiments'] = [
            (time.time()-random.randint(0, 10), random.uniform(-1, 1)) for i in range(50)]

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
