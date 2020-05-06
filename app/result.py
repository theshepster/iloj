class Result:

    def __init__(self, matchString, words, links):
        self.matchString = matchString
        self.wordLinks = zip(words, links)