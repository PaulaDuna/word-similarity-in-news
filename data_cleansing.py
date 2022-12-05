#!/usr/bin/env python3

import json
import re

with open("data/articles_search_2020.json", 'r') as f:
  articles_search = json.load(f)

clean_articles = []

for article in articles_search:
  clean_article = article.replace('[email\xa0protected]', '')
  clean_article = clean_article.lower()
  clean_article = re.sub(r'[^a-zñáéíóú ]', '', clean_article)
  for word in clean_article.split():
    if word.startswith('https://'):
      clean_article = clean_article.replace(word, '')
  clean_articles.append(clean_article)

with open("data/clean_articles_2020.json", 'w') as f:
  json.dump(clean_articles, f, indent = 2) 
