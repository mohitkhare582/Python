import requests
from bs4 import BeautifulSoup
import re


def games_onsite(sName):
    print("Getting the Games")
    for x in range(1, 4):
        url = "http://oceanofgames.com/post-sitemap" + str(x) + ".xml"
        source_code = requests.get(url)
        code_text = source_code.text
        soup = BeautifulSoup(code_text, "html.parser")
        for link in soup.find_all('loc'):
            gameName = link.string
            if re.search(sName, gameName, re.IGNORECASE):
                for char in '-':
                    gameName = gameName.replace(char, ' ')
                print(gameName[24:-15].upper())
                get_info(link.string)
                print('\n')


def get_info(url):
    source_code = requests.get(url)
    code_text = source_code.text
    soup = BeautifulSoup(code_text, "html.parser")
    for size in soup.find_all("li"):  # soup.find_all("li",{'class':'western'}):
        rstr = str(size.string)
        if rstr[:3] == "RAM" or rstr[:3] == "Ope" or rstr[:3] == "CPU" or rstr[:5] == "Setu" or rstr[:3] == "Har":
            print(rstr)


def game_search():
    gameName = str(input("Input Game to search :  "))
    games_onsite(gameName)


game_search()
