import requests
from bs4 import BeautifulSoup
import operator
import os
import heapq

link = 'http://www.w3newspapers.com/india/'
clear = lambda: os.system('cls')


def news_site():
    clear()
    site_list = {}
    top_terms = 7
    all_code = requests.get(link).text
    soup_ob = BeautifulSoup(all_code, 'html.parser')
    for websites in soup_ob.find_all('a', {'rel': 'nofollow'}):
        site_list[(websites.get('href'))] = websites.string
    for news_websites, name in site_list.items():
        print(name)
        get_news(news_websites, top_terms)


def get_news(url, top_terms):
    word_list = []
    news_code = requests.get(url).text
    soup_ob = BeautifulSoup(news_code, 'html.parser')
    for news in soup_ob.find_all('a'):
        news_article = str(news.string)
        word = news_article.lower().split()
        for terms in word:
            word_list.append(terms)
    get_fact(word_list, top_terms)


def get_fact(word_list, top_terms):
    facts = []
    for word in word_list:
        symbols = "!@#$%^&*()_+[]\"{}|;:\'<>?,.\/"
        for t in range(0, len(symbols)):
            word = word.replace(symbols[t], '')
            word = word.replace('none', '')
        if len(word) > 4:
            facts.append(str(word))

    show_facts(facts, top_terms)


def show_facts(facts, top_terms):
    terms = {}
    for word in facts:
        if word in terms:
            terms[word] += 1
        else:
            terms[word] = 1
            # for key, values in sorted(terms.items(), key=operator.itemgetter(1)):
            # print(key, values)
    print(heapq.nlargest(top_terms, terms, key=operator.itemgetter(1)))


news_site()
