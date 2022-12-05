#!/usr/bin/env python3

import json

with open("data/dates_search_2020.json", 'r') as f:
  dates_search = json.load(f)

with open("data/articles_wo_sw_2020.json", 'r') as f:
  articles_wo_sw = json.load(f)

print('There are', len(articles_wo_sw), 'elements in articles_wo_sw list.')

repeated_articles_index = []
for n, i in enumerate(articles_wo_sw):
  if i in articles_wo_sw[:n]:
    repeated_articles_index.append(n)

for index in repeated_articles_index:
  del dates_search[index]
  del articles_wo_sw[index]

print('But there are', len(articles_wo_sw), 'unique articles.')

with open("data/unique_articles_2020.json", 'w') as f:
  json.dump(articles_wo_sw, f, indent = 2) 

with open("data/unique_dates_2020.json", 'w') as f:
  json.dump(dates_search, f, indent = 2) 
