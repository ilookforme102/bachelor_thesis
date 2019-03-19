#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:59:00 2019

@author: macbook
"""
from textblob import TextBlob
import re
import string
def clean_data(tweet):
    # Remove HTML special entities (e.g. &amp;)
    tweet = re.sub(r'\&\w*;', '', tweet)
    # To lowercase
    tweet = tweet.lower()
    # using regex to clean the text by removing the link from text
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    # Remove Punctuation and split 's, 't, 've with a space for filter
    tweet = re.sub(r'[' + string.punctuation.replace('@', '') + ']+', ' ', tweet)
    # Remove words with 2 or fewer letters
    tweet = re.sub(r'\b\w{1,2}\b', '', tweet)
    # Remove whitespace (including new line characters)
    tweet = re.sub(r'\s\s+', ' ', tweet)
    # Remove single space remaining at the front of the tweet.
    tweet = tweet.lstrip(' ')
	#Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub('[\n]+', ' ', tweet)
	#Remove not alphanumeric symbols white spaces
    tweet = re.sub(r'[^\w]', ' ', tweet)
	#Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	#Remove :( or :)
    tweet = tweet.replace(':)','')
    tweet = tweet.replace(':(','')
	#trim
    tweet = tweet.strip('\'"')
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return tweet

def sentiment_tweets(tweet):
    model = TextBlob(clean_data(tweet))
    if model.sentiment.polarity > 0:
        return 1
    elif model.sentiment.polarity == 0:
        return 0
    else:
        return -1

data['Sentiment']= np.array([sentiment_tweets(tweet) for tweet in data['Tweets']])
display(data.head(10))

#anlysing the result of sentiment analysis:
pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] < 0]

print("percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))

#Topic modeling





