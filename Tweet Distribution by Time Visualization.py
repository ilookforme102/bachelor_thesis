#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 00:57:46 2019

@author: macbook
"""
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
