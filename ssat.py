from textblob import TextBlob as tb
import tweepy
import numpy as np

consumer_key = '2Ff1fwhV8PubQ9KRWg5BHNYVK'
consumer_secret = 'WHfqGZMdupXib0MpvyP7gmQskRLhb1F2mo65RDYVli58SwpqAs'
access_token = '843892947909332998-MlRVUB1H7D3xHw68eZLM2h8ONu4vkmM'
access_token_secret = 'bGnNDoHWEFLaqO2OSLoGkMiIKR4bKopwufxaZnGuAe9ha'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('Github')

analysis = None

for tweet in public_tweets:
    print(tweet.text)    
    analysis = tb(tweet.text)
    print(analysis.sentiment.polarity)
    
print('MÉDIA DE SENTIMENTO: ' + str(np.mean(analysis.sentiment.polarity)))
