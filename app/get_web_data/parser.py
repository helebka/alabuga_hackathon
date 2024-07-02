import requests
from bs4 import BeautifulSoup


def parser(url: str) -> str:
    src = requests.get(url)
    soup = BeautifulSoup(src.text, 'html')
    div = soup.find("div", class_="topic-body__content")
    return div.text
