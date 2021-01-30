import nltk
# requires punkt
class StockNameDetector:
    # the time window used for detecting prefixed tickers and counting them, in hours
    prefixCountingTimeWindow = 24 * 7
    # the amount of appearances of the prefixed ticker in the time window before they starts to be counted without a prefix
    symbolPrefixlessThreshold = 500
    def __init__(self):
        # should contain a dictionary of ticker keys mapped to a list of timestamps for prefixed instances
        self.knownStocks = {}
    def detectTickers(self, post):
        detected_symbols = []
        post_tokens = nltk.word_tokenize(post)
        # not perfect but will detect all stocks currently being hyped up
        for i,token in enumerate(post_tokens):
            if token == "$" and i+1 < len(post_tokens) and post_tokens[i+1] != "$" and not any(char.isdigit() for char in post_tokens[i+1]):
                if post_tokens[i+1] not in detected_symbols:
                    detected_symbols.append(post_tokens[i+1])
            elif token in self.knownStocks:
                if len(self.knownStocks[token]) >= prefixCountingTimeWindow:
                    detected_symbols.append(token)
        return detected_symbols
    def trimKnownStocks(self, time):
        for stock in self.knownStocks:
            for timestamp in knownStocks[stock]:
                if timestamp < time - prefixCountingTimeWindow * 60 * 60:
                    self.knownStocks[stock].remove[timestamp]

if __name__ == "__main__":
    detector = StockNameDetector()
    test_strings = ["LOL I BOUGHT $50 OF $GME HAHAH I'M GONNA MAKE $$$", "LOL I LOST ALL OF MY MONEY BUYING $AMC AND $BB :("]
    for s in test_strings:
        print(detector.detectTickers(s))