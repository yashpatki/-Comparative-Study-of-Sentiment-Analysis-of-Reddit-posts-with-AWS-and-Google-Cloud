from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
# import praw
# import argparse
import nltk.corpus
import nltk.tokenize
import nltk.sentiment
import time
from datetime import timedelta
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.downloader.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
comments = {'pos': {'count': 0, 'results': []},
            'neu': {'count': 0, 'results': []},
            'neg': {'count': 0, 'results': []}}
# count = 0
stop_words = set(stopwords.words('english'))


# PUT THE INPUT HERE
comment = "Oh, but didn't you know, being in a relationship means you totally have to just put up with their br..."

# removing the stopwords
filtered_comment = []
words = comment.split()
for word in words:
    if not word in stop_words:
        filtered_comment.append(word)
        comment1 = ' '.join(filtered_comment)
print(comment1)
score = analyzer.polarity_scores(comment1)

print(score)
