from textblob import TextBlob as tb
import tweepy
import numpy as np

consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token = 'your access token'
access_token_secret = 'your acess token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('Github')

analysis = None

for tweet in public_tweets:
    print(tweet.text)    
    analysis = tb(tweet.text)
    print(analysis.sentiment.polarity)
    
print('Average: ' + str(np.mean(analysis.sentiment.polarity)))
