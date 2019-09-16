# Stefanie Ochoa & Lilya Woodburn | Due 9/24/19

# Resources Used:
# 

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
import requests
from bs4 import BeautifulSoup

# global variables
url_seed =  'https://en.wikipedia.org/wiki/Puppy'
word_seed = 'dog'
porter = PorterStemmer()

def crawler(url): 
    page = requests.get(url_seed)

    if page.status_code == 200:
        print('sup')

        
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
            
web(1,'https://en.wikipedia.org/wiki/Puppy')


#############################################################################

# Lilya: copied the code from Net Instructions,
# just so we have it as a reference in text form

##from html.parser import HTMLParser
##from urllib.request import urlopen
##from urllib import parse
##
##class LinkParser(HTMLParser):
##    def handle_starttag(self, tag, attrs):
##        if tag == 'a':
##            for (key, value) in attrs:
##                if key == 'href':
##                    newUrl = parse.urljoin(self.baseUrl, value)
##                    self.links = self.links + [newUrl]
##
##    def getLinks(self, url):
##        self.links = []
##        self.baseUrl = url
##        response = urlopen(url)
##        if response.getheader('Content-Type')=='text/html':
##            htmlBytes = response.read()
##            htmlString = htmlBytes.decode("utf-8")
##            self.feed(htmlString)
##            return htmlString, self.links
##        else:
##            return "", []
##
##def spider(url, word, maxPages):
##    pagesToVisit = [url]
##    numberVisited = 0
##    foundWord = False
##    while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
##        numberVisited += 1
##        url = pagesToVisit[0]
##        pagesToVisit = pagesToVisit[1:]
##        try:
##            print(numberVisited, "Visiting:", url)
##            parser = LinkParser()
##            data, links = parser.getLinks(url)
##            if data.find(word) > -1:
##                foundWord = True
##            pagesToVisit = pagesToVisit + links
##            print(" **Success!** ")
##        except:
##            print(" **Failed!** ")
##    if foundWord:
##        print("The word ", word, " was found at ", url)
##    else:
##        print("Word not found")
