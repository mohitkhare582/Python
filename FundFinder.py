import requests
from bs4 import BeautifulSoup
import re

def top_funds(source_code):
    soup_ob = BeautifulSoup(source_code,"html.parser")
    for flink in soup_ob.find_all('a',{'class':'fundName'}):
        print(flink.string)


def fund_finder():
    url_main = "https://www.valueresearchonline.com/funds/"
    all_data = requests.get(url_main)
    text_data = all_data.text
    top_funds(text_data)

fund_finder()


