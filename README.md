# Word similarity in newspaper articles related to Covid-19

This project generates a database with newspaper articles from Pagina12 using web scraping, finds relevant articles with a keyword finder, cleans the dataset (removes punctuation, stopwords, etc) and finally tokenize the articles. Then, it uses Natural Language Processing (NLP) techniques to find most similar words to 'quarantine' ('cuarentena' in Spanish) in the articles, with a general model that contains all the data and also dividing articles by month.

## Project main goal

The aim of this project is to apply web scrapping and NLP techniques to the analysis of newspaper articles. In particular, it seeks to establish what concepts surround the word 'quarantine' in a particular newspaper.

## Summary

This project is divided into three phases: web scraping of newspaper articles to generate a news database; data cleansing and manipulation to prepare the articles for NLP models; and NLP models development, to find most similar words to 'quarantine'. Here is a brief summary of the steps you need to follow:

A) Newspaper articles web scraping:

1. **web_scraping_links**: uses BeautifulSoup to extract the links of all articles published during a certain period of time in the Pagina12 newspaper. 

2. **web_scraping_articles**: uses those links to extract the date, title and body of the articles and save them in separate lists. These database could be used for different types of projects.

3. **keywords_finder**: searches for keywords in the articles and saves the articles of interest and their dates in different lists. For this project, we will not be using the titles list.

B) Data cleansing and manipulation:

1. **data_cleansing**: removes email addresses and urls, converts text to lowercase and deletes all characters except letters.

2. **remove_stop_words_and_tokenize**: removes stopwords and transforms every article in a list of words (tokenizes the strings).

3. **check_duplicated_articles**: removes duplicated articles from the list of articles.

C) NLP models development:

1. **NLP_general_model**: uses Word2Vec to make a model that finds most similar words to a word of interest, in this case, 'quarantine'.

2. **NLP_model_by_month**: does the same, but grouping the articles by month.

## Data

The dataset of this work was built using articles from the newspaper [Pagina12](https://www.pagina12.com.ar/) published during 2020.

* All Python code is Python3.
