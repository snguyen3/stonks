from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import ast

class SentimentAnalyzer:
    sentimentIntensityAnalyzer = None

    def __init__(self):
        self.sentimentIntensityAnalyzer = SentimentIntensityAnalyzer()

    def getMessageIntensity(self, message):
        # Hmm.. To lemmatize, or not to lemmatize?
        # cleaned_tokens = self.remove_noise(word_tokenize(message))
        # scores = self.sentimentIntensityAnalyzer.polarity_scores(" ".join(cleaned_tokens))
        # for key in sorted(scores):
        #     print('Scores {0}: {1}, '.format(key, scores[key]), end='\n')

        scores = self.sentimentIntensityAnalyzer.polarity_scores(message)
        return scores['compound']

    def remove_noise(self, tokens, stop_words = ()):
        """
        :param tokens: (List) Tokens to clean (Remove Noise)
        :param stop_words: (Tuple) Words to ignore
        :return: (List) List of cleaned tokens
        """
        from nltk.stem.wordnet import WordNetLemmatizer
        from nltk.tag import pos_tag
        import re, string
        cleaned_tokens = []

        for token, tag in pos_tag(tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                           '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith("NN"):
                pos = 'n' # Noun
            elif tag.startswith('VB'):
                pos = 'v' # Verb
            else:
                pos = 'a' # Adjective

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens


class RedditDataParser:
    def getRedditData(self, filename, entries):
        retVal = []
        with open(filename, 'r', encoding="utf-8") as dataFile:
            lines = dataFile.readlines()
            for i in range(len(lines) if entries > len(lines) else entries):
                line = lines[i]
                retVal.append(ast.literal_eval(line))
        return retVal

    def parseData(self, data):
        retVal = []
        for entry in data:
            content = ""
            if('title' in entry.keys()):
                content = entry['title']
            else:
                content = ''
            parsedEntry = {
                'author': entry['author'],
                'content' : content,
                'date' : entry['created_utc'],
                'ups': entry['score']
            }
            retVal.append(parsedEntry)
        return retVal

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    parser = RedditDataParser()
    data = parser.getRedditData('wsb_8pct.txt', 80000)
    parsed_data = parser.parseData(data)
    with open("wsb-sample.csv", "w") as of:
        of.writelines(str(line) + '\n' for line in parsed_data)
    exit()


    example_posts = ["$TSLA TO THE MOON BABEEEEE", "SELL SELL SELL AAAAAAAAAAAAAA"]
    for entry in example_posts:
        entry = entry.lower()
    for i,post in enumerate(example_posts):
        intensity = analyzer.getMessageIntensity(post)
        print("{} : {}\n".format(i, intensity))