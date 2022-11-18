#!/usr/bin/env python3

import json
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import os

with open("data/url_list_2020.json", 'r') as f:
  url_list = json.load(f)

dates = []
titles = []
articles = []
total_urls = len(url_list)

for url in url_list:
    try:
        verified_urls = len(dates)
        print('\r', 'Current progress:', np.round(verified_urls * 100 / total_urls), '%', flush = True, end = " ")
        article_url = "https://www.pagina12.com.ar" + url
        req = requests.get(article_url)
        soup = BeautifulSoup(req.content, "html.parser")
        date = soup.find('div', {'class':'date modification-date'}).get_text().split(' - ')[0]
        dates.append(date)
        title = soup.find('h1').get_text()
        titles.append(title)
        article = soup.find('div', {'class':'article-text'}).get_text(strip = True, separator = ' ')
        articles.append(article)
    except AttributeError:
        print('\r', 'Sleep for 60 seconds!', flush = True, end = " ")
        time.sleep(60)
        req = requests.get(article_url)
        soup = BeautifulSoup(req.content, "html.parser")
        date = soup.find('div', {'class':'date modification-date'}).get_text().split(' - ')[0]
        dates.append(date)
        title = soup.find('h1').get_text()
        titles.append(title)
        article = soup.find('div', {'class':'article-text'}).get_text(strip = True, separator = ' ')
        articles.append(article)
    except (ChunkEncodingError, ConnectionError) as e:
        pass

path = "data/"
if not os.path.exists(path):
    os.makedirs(path)

with open("data/dates_2020.json", 'w') as f:
  json.dump(dates, f, indent = 2) 

with open("data/titles_2020.json", 'w') as f:
  json.dump(titles, f, indent = 2) 

with open("data/articles_2020.json", 'w') as f:
  json.dump(articles, f, indent = 2) 
