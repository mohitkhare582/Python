import requests
from bs4 import BeautifulSoup
import re


def games_onsite(sName):
    print("Getting the Games")
    page = 1

    while 270 >= page:
        url = "http://oceanofgames.com/page/" + str(page)
        source_code = requests.get(url)
        code_text = source_code.text
        soup = BeautifulSoup(code_text, "html.parser")
        for link in soup.find_all('a', {'rel': 'bookmark'}):
            gameLink = link.get('href')
            gameName = link.string
            if re.search(sName, gameName, re.IGNORECASE):
                print(gameName)
                get_info(gameLink)
                print('\n')
                # fw.write(gameName[:-14] + "\n")
        page += 1

    # print("Open File to see Games")


def get_info(url):
    source_code = requests.get(url)
    code_text = source_code.text
    soup = BeautifulSoup(code_text, "html.parser")
    for size in soup.find_all("li"):  # soup.find_all("li",{'class':'western'}):
        rstr = str(size.string)
        if rstr[:3] == "RAM" or rstr[:3] == "Ope" or rstr[:3] == "CPU" or rstr[:3] == "Set" or rstr[:3] == "Har":
            print(rstr)


def game_search():
    gameName = str(input("Input Game to search :  "))
    games_onsite(gameName)


game_search()
