import requests
from bs4 import BeautifulSoup
import operator
import os
import heapq

link = 'http://www.indiapress.org/index.php/English/400x60'
clear = lambda: os.system('cls')


def news_site():
    site_list = {}
    all_code = requests.get(link).text
    soup_Ob = BeautifulSoup(all_code, 'html.parser')
    for websites in soup_Ob.find_all('a', {'target': '_blank'}):
        site_list[(websites.get('href'))] = websites.string
    for news_websites in site_list:
        print(site_list[websites])
        get_news(news_websites)


def get_news(url):
    clear()
    word_list = []
    news_code = requests.get(url).text
    soup_ob = BeautifulSoup(news_code, 'html.parser')
    for news in soup_ob.find_all('a'):
        news_article = str(news.string)
        word = news_article.lower().split()
        for terms in word:
            word_list.append(terms)
    get_fact(word_list)


def get_fact(word_list):
    facts = []
    for word in word_list:
        symbols = "!@#$%^&*()_+[]\"{}|;:\'<>?,.\/"
        for t in range(0, len(symbols)):
            word = word.replace(symbols[t], '')
            word = word.replace('none', '')
        if len(word) > 3:
            facts.append(str(word))

    show_facts(facts)


def show_facts(facts):
    terms = {}
    for word in facts:
        if word in terms:
            terms[word] += 1
        else:
            terms[word] = 1
            # for key, values in sorted(terms.items(), key=operator.itemgetter(1)):
            # print(key, values)
    print(heapq.nlargest(5, terms, key=operator.itemgetter(1)))


news_site()
