# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:08:07 2019

@author: Lordd
"""

import tweepy
from textblob import TextBlob

consumer_key = 'XrnhlrEPZILuKdhEyb7CfJo87'
consumer_secret = 'xgHmvBeoOs2m5NVbS8qU5SPvVI6WSWnYtS5j44Odjymna0q9KY'

access_token = '1051143815690477568-X437UVETjHeaGwsA20gfodnInGsiBZ'
access_token_secret = 'wDqckqcc9GE0CxTV1GwkRkcOQWSwY8XMQ3pdY273NxbMP'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Facebook')

for tweets in public_tweets:
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)
