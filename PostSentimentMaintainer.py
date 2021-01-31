import json, time, cProfile
import WSBSentimentAnalyzer, StockNameDetector
import ast
analyzer = WSBSentimentAnalyzer.SentimentAnalyzer()
detector = StockNameDetector.StockNameDetector()
reddit_posts_file = "wsb-sample.csv"
class PostSentimentMaintainer:
    analyzer = analyzer
    bin_size = 3 # hours
    reddit_posts_file = reddit_posts_file
    post_sentiments_file = "post_sentiments.json"
    def __init__(self):
        pass
    def recordPostSentiment(self, parsed_post):
        bin_timestamp = str(parsed_post['date'] - (parsed_post['date'] % (self.bin_size * 60 * 60)))
        with open(self.post_sentiments_file, "r+") as psf:
            try:
                parsed_psf = json.load(psf)
            except ValueError:
                parsed_psf = {}
            if bin_timestamp in parsed_psf.keys():
                parsed_psf[bin_timestamp]['entries'].append({'sentiment':self.analyzer.getMessageIntensity(parsed_post['content']) ,'post':parsed_post})
            else:
                parsed_psf[bin_timestamp] = {'entries':[],'composite':None}
            psf.seek(0)
            psf.truncate()
            json.dump(parsed_psf, psf)

    def calculateBinSentiment(self, bin_timestamp, print_option=False):
        bin_sentiment = 0
        with open(self.post_sentiments_file, "r+") as psf:
            try:
                parsed_psf = json.load(psf)
            except ValueError:
                parsed_psf = {}
            if bin_timestamp in parsed_psf.keys():
                num_entries = len(parsed_psf[bin_timestamp]['entries'])
                for entry in parsed_psf[bin_timestamp]['entries']:
                    if entry['sentiment'] is None:
                        entry['sentiment'] = self.analyzer.getMessageIntensity(entry['post']['content'])
                    bin_sentiment += entry['sentiment']/num_entries
            else:
                print("pick an actually valid timestamp please")
            parsed_psf[bin_timestamp]['composite'] = bin_sentiment
            if print_option:
                print(parsed_psf[bin_timestamp['composite']])
            psf.seek(0)
            psf.truncate()
            json.dump(parsed_psf, psf)

    def calculateAllSentiments(self):
        with open(self.reddit_posts_file, 'r', encoding="utf-8") as rpf:
            lines = rpf.readlines()
            for i, line in enumerate(lines):
                self.recordPostSentiment(ast.literal_eval(line))
        with open(self.post_sentiments_file, "r+") as psf:
            try:
                parsed_psf = json.load(psf)
            except ValueError:
                parsed_psf = {}
            timestamps = parsed_psf.keys()
        for t in timestamps:
            self.calculateBinSentiment(t, True)


def getSentimentData(tickers, period, interval):
    retVal = []
    # in seconds
    valid_date_ranges = {'1D':86400, '1M':2629800, '6M':2629800*6, '1Y':31557600, 'YTD':time.time() % 31557600, 'ALL':time.time()}
    valid_time_intervals = {'1m':60, '2m':120, '5m':300, '15m':900, '30m':1800,'60m':3600,'90m':4800,'1h':3600,'1d':3600*24,'5d':3600*24*5,'1wk':3600*24*7,'1mo':2629800}
    ticker_filtered_lines = {}
    ticker_binned_lines = {}
    if period in valid_date_ranges.keys():
        period_seconds = valid_date_ranges[period]
    else:
        period_seconds = valid_date_ranges['1M']

    if interval in valid_time_intervals.keys():
        interval_seconds = valid_time_intervals[interval]
    else:
        interval_seconds = valid_time_intervals['1h']

    starting_time = time.time() - period_seconds

    for t in tickers:
        retVal.append({'name':t, 'data':[]})
        ticker_filtered_lines[t] = []
        ticker_binned_lines[t] = {}

    max_lines = 1000
    update_interval = 100
    with open(reddit_posts_file, 'r', encoding="utf-8") as rpf:
        print("Reading/filtering lines from file...")
        lines = rpf.readlines()
        for i, line in enumerate(lines):
            if i > max_lines:
                break
            if i % update_interval == 0 and i != 0:
                percent_done = 100*(i/max_lines)
                print(str(percent_done) + "% done")
            parsed_line = ast.literal_eval(line)
            if parsed_line['date'] < starting_time:
                continue
            referenced_tickers = detector.detectTickers(parsed_line['content'])
            for t in referenced_tickers:
                if t in tickers:
                    ticker_filtered_lines[t].append(parsed_line)

    for t in tickers:
        print("Sorting " + t + "-related lines into bins...")
        for pl in ticker_filtered_lines[t]:
            if str(pl['date'] - (pl['date'] % interval_seconds)) not in ticker_binned_lines[t].keys():
                ticker_binned_lines[t][str(pl['date'] - (pl['date'] % interval_seconds))] = {'composite':0, 'entries':[]}
            ticker_binned_lines[t][str(pl['date'] - (pl['date'] % interval_seconds))]['entries'].append({'post':pl,'sentiment':None})
        print("Calculating sentiment for each " + t + "-related line bin...")
        for timestamp,bin in ticker_binned_lines[t].items():
            bin_sentiment = 0
            num_entries = len(bin['entries'])
            for entry in bin['entries']:
                if entry['sentiment'] is None:
                    entry['sentiment'] = analyzer.getMessageIntensity(entry['post']['content'])
                bin_sentiment += entry['sentiment']/num_entries
            bin['composite'] = bin_sentiment
            for d in retVal:
                if d['name'] == t:
                    d['data'].append([timestamp, bin['composite']])
    return retVal
if __name__ == "__main__":
    psm = PostSentimentMaintainer()
    #cProfile.run("print(getSentimentData(['GME'],'5Y','3M'))")
    print(getSentimentData(['GME'], '5Y', '3M'))