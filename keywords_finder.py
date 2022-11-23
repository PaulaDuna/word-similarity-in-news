#!/usr/bin/env python3

import json

with open("data/dates_2020.json", 'r') as f:
  dates = json.load(f)

with open("data/titles_2020.json", 'r') as f:
  titles = json.load(f)

with open("data/articles_2020.json", 'r') as f:
  articles = json.load(f)

keywords = ["coronavirus", "covid", "cov-2", "cuarentena"]
dates_search = []
titles_search = []
articles_search = []

for date, title, article in zip(dates, titles, articles):
  for word in keywords:
    if word.lower() in article.lower() and title not in titles_search:
      dates_search.append(date)
      titles_search.append(title)
      articles_search.append(article)

with open("data/dates_search_2020.json", 'w') as f:
  json.dump(dates_search, f, indent = 2) 

with open("data/articles_search_2020.json", 'w') as f:
  json.dump(articles_search, f, indent = 2) 
