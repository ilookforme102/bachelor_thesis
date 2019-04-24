#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:27:56 2019

@author: macbook
"""
import numpy as np
from gensim import corpora, models, similarities
import warnings
warnings.filterwarnings("ignore")
#Creating a corpus of text data
corpus = []
def clean_data(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    # Remove HTML special entities (e.g. &amp;)
    tweet = re.sub(r'\&\w*;', '', tweet)
    # To lowercase
    tweet = tweet.lower()
    # using regex to clean the text by removing the link from text
    tweet = re.sub('@[^\s]+','',tweet)
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
    return tweet

for tweet in data["Tweets"]:
    clean_data(tweet)
    corpus.append(tweet)
import nltk   
import gensim
import logging
import tempfile
import os
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))

from gensim import corpora
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#from command line run: python -m nltk.downloader stopwords

from nltk.corpus import stopwords
from string import punctuation
#cleaning da
# remove common words and tokenize
list1 = ['RT','rt']
stoplist = stopwords.words('english') + list(punctuation) + list1

texts = [[word for word in str(document).lower().split() if word not in stoplist] for document in corpus]
dictionary = corpora.Dictionary(texts)
# store the Trump dictionary
dictionary.save(os.path.join(TEMP_FOLDER, 'trump.dict'))
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'trump.mm'), corpus)

from gensim import corpora, models, similarities

tfidf_md = models.TfidfModel(corpus)
corpus_tfidf_md = tfidf_md[corpus]

#main part of LDA topic modeling:
number_topics = 5
lda_model = models.LdaModel(corpus, id2word=dictionary, num_topics=number_topics)
corpus_lda = lda_model[corpus_tfidf_md]
#Show first n important word in the topics:
lda_model.show_topics(number_topics,5)
from collections import OrderedDict

data_lda = {i: OrderedDict(lda_model.show_topic(i,25)) for i in range(number_topics)}
#data_lda

import pandas as pd

df_lda = pd.DataFrame(data_lda)
print(df_lda.shape)
df_lda = df_lda.fillna(0).T
print(df_lda.shape)
df_lda