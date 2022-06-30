from logging import raiseExceptions
from re import sub
import requests
from bs4 import BeautifulSoup
import pprint


def import_data(pages):
    links = []
    subtext = [] 

    for page in pages:
        res = requests.get(page)
        soup = BeautifulSoup(res.text, 'lxml')
        links_a = soup.select('.titlelink')
        subtext_a = soup.select('.subtext')
        links.extend(links_a)
        subtext += subtext_a

    return links, subtext

def sort_news(news):
    return sorted(news, key= lambda k:k['votes'], reverse=True)

def create_custom_news(links, subtext):
    news = []

    for idx, item in enumerate(links):
        title = links[idx].getText() # get link's text
        href = links[idx].get('href', None)
        # point = votes[idx].getText().split(" ")[0]
        if subtext[idx].select('.score'):
            point = int(subtext[idx].select('.score')[0].getText().replace(" points", ''))
            if point < 100:
                continue
            news.append({'title' : title, 'href' : href, 'votes': point})
    
    return sort_news(news)

def main():
    urls = ["https://news.ycombinator.com/", "https://news.ycombinator.com/news?p=2"]
    links, subtext = import_data(urls)
    data = create_custom_news(links, subtext)
    pprint.pprint(data)

main()