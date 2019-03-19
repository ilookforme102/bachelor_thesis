# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 02:45:39 2018

@author: ILOOKFORME102
"""
import tweepy
import csv
from tweepy import OAuthHandler

consumer_key = 'HcfzNWaWkDSSrSKkWSSzk6SIH'
consumer_secret = '2KUAvtpRu4dzjilbpWhkCrEUAly71WQvFhj2ptjqgURYWEqjp1'
access_token = '715066304848338944-4JZgsQ3KeWfo2oncG1B3q4XzgpjXJDY'
access_token_secret = 'PZrCebFpZo7IgdKd0FDqQqTxSeCLIISyOiX5v3vBGhWEr'

tweet_name = "realDonaldTrump"
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    alltweets = []  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(id = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print('getting tweets before {}'.format(oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print ("...{} tweets downloaded so far".format(len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id,len(tweet.text),tweet.text, tweet.created_at,tweet.source, tweet.favorite_count,tweet.retweet_count] for tweet in alltweets]

    #write the csv  
    with open('{}_tweets.csv'.format(screen_name), 'wt') as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Length","Tweets","Date","Source","Likes","Retweets"])
        writer.writerows(outtweets)

    pass
if __name__ == '__main__':
	get_all_tweets(tweet_name)
