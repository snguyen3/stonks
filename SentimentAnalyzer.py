from nltk.sentiment.vader import SentimentIntensityAnalyzer

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


if __name__ == "__main__":
    from newspaper import Article
    articleUrls = [
                "https://www.google.com/search?sxsrf=ALeKk0061gAZmAyLBMmrDScUBxmoeOUtmg%3A1604628562744&ei=UrCkX6T-LKapytMPy9qzoAU&q=epal+gg+news&oq=epal+gg+news&gs_lcp=CgZwc3ktYWIQAzIFCCEQoAEyBQghEKABMgUIIRCgAToECAAQRzoFCCEQqwJQ6A1YlRNg6RZoAXADeACAAVuIAfACkgEBNZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwik7-mb6-zsAhWmlHIEHUvtDFQQ4dUDCA0&uact=5",
                "https://medium.com/@luciahuahau/a-new-profession-epal-is-born-during-the-covid-19-33e063dba15f",
                "https://templeofgeek.com/rebels-discuss-epal-gg/",
                "https://www.bbc.com/future/article/20140728-why-is-all-the-news-bad",
                "https://abc7ny.com/society/photos-the-aftermath-of-9-11/291557/"]
    analyzer = SentimentAnalyzer()

    articleText = ""
    for articleUrl in articleUrls:
        article = Article(articleUrl)
        article.download()
        article.parse()
        # End with a period to separate different articles
        articleText = articleText + article.text + " . "

        intensity = analyzer.getMessageIntensity(articleText)
        print("{} : {}\n".format(articleUrl, intensity))

    # msg = "Nearly 3,000 people lost their lives on 9/11 during the worst terrorist attack in recorded history. Since then, several thousand people have died because of 9/11-related illnesses and cancers, including residents who lived in the area in the months that followed the attacks.  Many downtown residents never connect their breathing the 9/11 dust and fumes to cancers or other illnesses that are diagnosed years or even over a decade later. "
    # intensity = analyzer.getMessageIntensity(msg)
    # print("{} : {}\n".format("9/11", intensity))
