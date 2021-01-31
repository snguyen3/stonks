
import math


def main():
    print(getStockData("GME", "5y", "3mo"))

    # Send stonks in the format
    # return stonks in the format


def getSubredditData(subredditName, dateRange):
    return None


"""
@param1 - tickers : string - The name of the ticker (stock name) to pull data for
@param2 - dateRange : list of string - The time to pull data from : Example: ["01-01-2020", "01-01-2021"]
@param3: interval - The date interval (1 minute, 5 minutes, 30 minutes, etc.)
def getSentimentData(tickers : list of string, dateRange: list of string, interval: string)
"""


def getSentimentData(tickers, dateRange, interval):
    retVal = [{}]

    """
    return sentiment scores over time
    [{
        'name':'ticker1'
        'data':[[x,y],[x,y],[x,y],[x,y]]
    },
    {
        'ticker':'name2',
        'data':[[x,y],[x,y],[x,y],[x,y]]
    }]
    """


"""
@param1 - tickers : string - The name of the ticker (stock name) to pull data for
@param2 - period : Period to pull from (see below)
@param3: interval - Interval to pull from (see below)
def getStockData(tickers : list of string, dateRange: list of string, interval: string)
"""


def getStockData(tickers, period, interval):
    retVal = []
    import yfinance as yf

    for ticker in tickers:
        series = {
            "name": ticker,
            "data": []
        }
        data = yf.download(
            # tickers list or string as well
            tickers=ticker,

            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            period=period,

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval=interval,

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by='ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust=True,

            # download pre/post regular market hours data
            # (optional, default is False)
            prepost=True,

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads=True,

            # proxy URL scheme use use when downloading?
            # (optional, default is None)
            proxy=None
        )
        data = data.reset_index()

        for i in range(0, data.shape[0]):
            try:
                x = data.iloc[i]['Date']
                y = data.iloc[i]['Open']
                if(not math.isnan(y)):
                    series['data'].append([x, y])
            except:
                pass
        retVal.append(series)
    """
    return stock scores over time
    [{
        'name':'ticker1'
        'data':[[x,y],[x,y],[x,y],[x,y]]
    },
    {
        'name':'ticker2',
        'data':[[x,y],[x,y],[x,y],[x,y]]
    }]
    """

    return retVal


if __name__ == "__main__":
    main()
