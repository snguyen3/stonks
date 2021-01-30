import json
import time

class StockListMaintainer:
    prefixCountingTimeWindow = 24 * 7
    known_stocks_file = "known_stocks.json"
    def __init__(self):
        pass
    def trimKnownStocks(self, time):
        with open(self.known_stocks_file, "r+") as ksf:
            known_stocks_changed = False
            try:
                known_stocks = json.load(ksf)
            except ValueError:
                known_stocks = {}
            for stock in known_stocks:
                for timestamp in known_stocks[stock]:
                    if timestamp < time - (self.prefixCountingTimeWindow * 60 * 60):
                        known_stocks[stock].remove(timestamp)
                        known_stocks_changed = True
            if known_stocks_changed:
                ksf.seek(0)
                ksf.truncate()
                json.dump(known_stocks, ksf)

if __name__ == "__main__":
    maintainer = StockListMaintainer()
    maintainer.trimKnownStocks(time.time())