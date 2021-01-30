import nltk
import json
import time
import csv
import StockListMaintainer


# requires punkt
maintainer = StockListMaintainer.StockListMaintainer()
class StockNameDetector:
    known_stocks_file = "known_stocks.json"
    valid_stock_symbols_file = "valid_stock_symbols.csv"
    vssf_arr = []
    def __init__(self):
        pass
    def detectTickers(self, post):
        with open(self.valid_stock_symbols_file, "r") as vssf:
            with open(self.known_stocks_file, "r+") as ksf:
                known_stocks_changed = False
                try:
                    known_stocks = json.load(ksf)
                except ValueError:
                    known_stocks = {}
                valid_stock_symbol_reader = csv.reader(vssf, delimiter="\t")
                detected_symbols = []
                post_tokens = nltk.word_tokenize(post)
                for t in post_tokens:
                    if not t in detected_symbols:
                        if t in known_stocks:
                            detected_symbols.append(t)
                            known_stocks[t].append(time.time())
                            known_stocks_changed = True
                        if not t in known_stocks:
                            if(len(self.vssf_arr) == 0):
                                self.vssf_arr = [s[0] for s in valid_stock_symbol_reader]
                            if t in self.vssf_arr:
                                detected_symbols.append(t)
                                known_stocks[t] = [time.time()]
                                known_stocks_changed = True
                                #print(t, "accepted as ticker")
                            else:
                                pass
                                #print(t, "not accepted as ticker")
                if known_stocks_changed:
                    ksf.seek(0)
                    ksf.truncate()
                    json.dump(known_stocks, ksf)
        return detected_symbols

if __name__ == "__main__":
    detector = StockNameDetector()
    test_strings = ["LOL I BOUGHT $50 OF $GME HAHAH I'M GONNA MAKE $$$", "LOL I LOST ALL OF MY MONEY BUYING $AMC AND $BB :("]
    for s in test_strings:
        print(detector.detectTickers(s))