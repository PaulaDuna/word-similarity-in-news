#!/usr/bin/env python3

import json
import collections
import multiprocessing
from gensim.models import Word2Vec

with open("data/unique_articles_2020.json", 'r') as f:
  articles = json.load(f)

with open("data/unique_dates_2020.json", 'r') as f:
  dates = json.load(f)

#Dictionary with articles by month
months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

dct_articles = collections.OrderedDict()
for month in months:
    articles_by_month = []
    for date, article in zip(dates, articles):
        if month == date.split()[2]:
            articles_by_month.append(article)
    dct_articles[month] = articles_by_month

#Most similar words by month
dct_model = collections.OrderedDict()
cores = multiprocessing.cpu_count()

for key in dct_articles:
    model = Word2Vec(dct_articles[key], vector_size = 100, window = 5, min_count = 3, workers = cores - 1)
    dct_model[key] = model.wv.most_similar('cuarentena')[:10]

for key in dct_model:
    print(key, ':', sep = '')
    for word in dct_model[key]:
        print(word[0], end = ' ')
    print('\n')
