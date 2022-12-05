#!/usr/bin/env python3

import json
import multiprocessing
from gensim.models import Word2Vec
import pprint

with open("data/unique_articles_2020.json", 'r') as f:
  articles = json.load(f)

cores = multiprocessing.cpu_count()
model = Word2Vec(articles, vector_size = 100, window = 5, min_count = 50, workers = cores - 1)

#Vocabulary
print('The model used', len(model.wv.key_to_index), 'words as vocabulary.\n')

#Most frequent words in the articles dataset
print('The 10 most frequent words in the articles and their number of occurrences were:\n')
most_freq = model.wv.index_to_key[:10]
for word in most_freq:
    print(word, ': ', model.wv.get_vecattr(word, "count"), sep = '')

#Most similar words
similar_words = [word for word, value in model.wv.most_similar('cuarentena')[:10]]
print('\nThe 10 most similar words to \'quarantine\' in the articles were:\n')
pprint.pprint(similar_words)
