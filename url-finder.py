# https://docs.python.org/2/library/urllib2.html


import requests
import nltk
import re
import random
from urllib.request import urlopen
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn
from bs4 import BeautifulSoup

def getLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    links = []

    for link in soup.findAll('a'):
        temp = str(link.get('href'))
        search = '/wiki/'
        if temp.startswith(search):
            http = 'https://en.wikipedia.org'
            new_url = http+temp
            if new_url not in links:
                links.append(new_url)

    new_links = []
    new_urls = []
    n = 0
    while not n == 5:
        rand_num = random.randrange(0, len(links), 1)
        rand_url = links[rand_num]
        new_urls.append(rand_url)
        n += 1
    
    return new_urls

print(getLinks("https://en.wikipedia.org/wiki/Magliocca") )
