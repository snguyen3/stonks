
def main():

    

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
@param2 - dateRange : list of string - The time to pull data from : Example: ["01-01-2020", "01-01-2021"]
@param3: interval - The date interval (1 minute, 5 minutes, 30 minutes, etc.)
def getStockData(tickers : list of string, dateRange: list of string, interval: string)
"""
def getStockData(tickers, dateRange, interval):
    retVal = [{}]

    """
    return stock scores over time
    [{
        'name':'ticker1'
        'data':[[x,y],[x,y],[x,y],[x,y]]
    },
    {
        'ticker':'name2',
        'data':[[x,y],[x,y],[x,y],[x,y]]
    }]
    """

if __name__ == "__main__":
    main()