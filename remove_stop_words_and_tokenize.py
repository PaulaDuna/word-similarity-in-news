#!/usr/bin/env python3

import json
from nltk.corpus import stopwords

with open("data/clean_articles_2020.json", 'r') as f:
  clean_articles = json.load(f)

articles_wo_sw = []
stopwords = stopwords.words('spanish')

for article in clean_articles:
  article_wo_sw = []
  for word in article.split():
    if word not in stopwords:
      article_wo_sw.append(word)
  articles_wo_sw.append(article_wo_sw)

with open("data/articles_wo_sw_2020.json", 'w') as f:
  json.dump(articles_wo_sw, f, indent = 2) 
