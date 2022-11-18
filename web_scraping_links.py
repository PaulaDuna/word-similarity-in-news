#!/usr/bin/env python3

from datetime import date, timedelta
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
import os

start_date = date(2020, 1, 1)
final_date = date(2020, 12, 31)
delta = timedelta(days = 1)
total_days = (final_date - start_date).days
url_list = []

while start_date <= final_date:
  days_left = (final_date - start_date).days
  print('\r', 'Current progress:', np.round(100 - days_left * 100 / total_days), '%', flush = True, end = " ")
  url = "https://www.pagina12.com.ar/edicion-impresa/" + start_date.strftime("%d-%m-%Y")
  req = requests.get(url)
  soup = BeautifulSoup(req.content, "html.parser")
  try:
    for element in soup.findAll('div', {'class':'article-list-container'})[0].findAll('h2'):
      for element_w_link in element.findAll('a', href = True, attrs = {'class': None}):
        url = element_w_link['href']
        url_list.append(url)
    start_date += delta
  except IndexError:
    start_date += delta

path = "data/"
if not os.path.exists(path):
    os.makedirs(path)

with open("data/url_list_2020.json", 'w') as f:
  json.dump(url_list, f, indent = 2) 
