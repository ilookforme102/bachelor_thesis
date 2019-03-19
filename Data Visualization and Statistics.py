#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 00:57:46 2019

@author: macbook
"""
import numpy as np
import pandas as pd
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.graph_objs as go

data = pd.read_csv('realDonaldTrump_tweets.csv',encoding="utf-8")
data = data.assign(Date=pd.to_datetime(data.Date)).drop('ID', axis='columns')
data['Date'] = pd.to_datetime(data['Date'], format='%y-%m-%d %H:%M:%S')
dataT = data['Date']

trace = go.Histogram(
    x=dataT,
    marker=dict(
        color='blue'
    ),
    opacity=0.75
)

layout = go.Layout(
    title="Donald Trump's Tweets Distribution",
    height=450,
    width=1200, 
    xaxis=dict(
        title='Time'
    ),
    yaxis=dict(
        title='Number of Tweets'
    ),
    bargap=0.3,
)

data_trace = [trace]

fig = go.Figure(data=data_trace, layout=layout)
plot(fig)

 """ Some basic statistic for the lenght of tweet """
mean_length = np.mean(data['Length']) 
print(mean_length)
max_like = np.max(data['Likes'])
max_retweet = np.max(data['Retweets'])

#Print out the tweets which has the most likes and retweets:
max_like_index = data[data.Likes == max_like].index[0]
max_retweet_index  = data[data.Retweets == max_retweet].index[0]

# Max likes:
print("Most favorite tweet by number of likes: \n{}".format(data['Tweets'][max_like_index]))
print("Quantity: {}".format(max_like))
print("{} characters.\n".format(data['Length'][max_like_index]))

# Max retweets:
print("Most favorite tweet by number of retweets: \n{}".format(data['Tweets'][max_retweet_index]))
print("Quantity: {}".format(max_retweet))
print("{} characters.\n".format(data['Length'][max_retweet_index]))


#time series tracking the change of likes,retweets and the length of tweet 

len_by_time = pd.Series(data=data['Length'].values, index=data['Date'])
likes_by_time = pd.Series(data=data['Likes'].values, index=data['Date'])
retweets_by_time = pd.Series(data=data['Retweets'].values, index=data['Date'])

#visualization 

len_by_time.plot(figsize=(16,4), label="Length", legend=True, color='r')
# visualizing the time series of number of likes and retweets 
likes_by_time.plot(figsize=(16,4), label="Likes", legend=True,color='g')
retweets_by_time.plot(figsize=(16,4), label="Retweets", legend=True,color='b');