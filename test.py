
# Resources
# https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer
# https://www.geeksforgeeks.org/python-stemming-words-with-nltk/
# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

import requests
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn
from bs4 import BeautifulSoup
import random
from urllib.request import urlopen

#page = requests.get("https://en.wikipedia.org/wiki/Magliocca")

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
    #print(links)
    
    new_links = []
    new_urls = []
    n = 0

    # if each seed begets 20 links, the min num of possible duplicates is 100
    while not n == 5:
        rand_num = random.randrange(0, len(links), 1)
        rand_url = links[rand_num]
        new_urls.append(rand_url)
        n += 1
    
    return new_urls


def ourCrawler(url):
    stop_words = set(stopwords.words('english'))
    page = requests.get(url)
    porter = PorterStemmer()

    #print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    page.status_code
    #master_dict = PyDictionary()
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text = text.lower()

    tokenizer = RegexpTokenizer(r'\w+')

    word_tokens = tokenizer.tokenize(text)

    tagged = nltk.pos_tag(word_tokens) # determine word parts
    nouns = [] # initialize a list

    for tkn in tagged:
        word = tkn[0] # grabs word
        gram = tkn[1] # grabs word's part of speech
        if gram[-len(gram)] == 'N':
            if len(word) > 1:
                nouns.append(word)

    filtered_sentence = [w for w in nouns if not w in stop_words] 
  
    filtered_sentence = [] 

    for w in nouns: 
        if w not in stop_words:
            w = porter.stem(w)
            filtered_sentence.append(w)
        
    word_list = {}

    for i in range(len(filtered_sentence)):
        if not filtered_sentence[i] in word_list.keys():
            word_list[filtered_sentence[i]] = 1
        else:
            word_list[filtered_sentence[i]] += 1 

    #pages_crawled += 1

    return word_list

def writeIndex(index):
    f = open("index.txt", "w+")

    for x in index:
        f.write(x)
        f.write('\n')
        list_of_tuples = index[x]

        for y in list_of_tuples:
            f.write(str(y[0]) + " " + str(y[1])+'\n')
    f.close()
    return

def writeURL(li):
    f = open("urlDoc.txt", "w+")
    j = 0
    print(len(li))
    while j < len(li):
        f.write(str(j))
        f.write('\n')
        f.write(li[j] + '\n')
        j += 1 
    f.close()
    return

def searchDoc(search_term):
    # search_term is a string, can be either of the query terms
    f = open("index.txt", "r+")

    temp = f.readline()

    while temp != search_term:
        temp = f.readline()

    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    searchDict = {}

    # temp starts keeping track of numbers now
    temp = f.readline()

    # add document IDs and word occurrences to searchDict as (k, v) pairs
    #while temp.startswith("0") or temp.startswith("1") or temp.startswith("2") or temp.startswith("3") or temp.startswith("4") or temp.startswith("5") or temp.startswith("6") or temp.startswith("7") or temp.startswith("8") or temp.startswith("9"):
    while temp[:1] in digits:
        kv = temp.split()
        searchDict[kv[0]] = kv[1]
        temp = f.readline
    # cast to ints?
    
    f.close()

    for keys,values in searchDict.items():
        print(keys)
        print(values)

    # returns dict of document IDs and word occurrences for search_term
    return searchDict

def main():
    
    pages_crawled = 0

    '''
    seedList = ["https://en.wikipedia.org/wiki/Magliocca",
                "http://en.wikipedia.org/wiki/Puppy",
                "https://en.wikipedia.org/wiki/Samoa_Breweries",
                "https://en.wikipedia.org/wiki/FC_Karlivka",
                "https://en.wikipedia.org/wiki/Raam_Punjabi",
                "https://en.wikipedia.org/wiki/Martian_Heartache",
                "https://en.wikipedia.org/wiki/Robert_C._Helmer",
                "https://en.wikipedia.org/wiki/Ivo_den_Bieman",
                "https://en.wikipedia.org/wiki/Editora_Fundamento",
                "https://en.wikipedia.org/wiki/Thomas_Mesnier"]
    '''
    seedList = ["https://en.wikipedia.org/wiki/Magliocca",
                "http://en.wikipedia.org/wiki/Puppy"]
    
    new_links = []

    keywords = ["and","not","or"]

    '''
    while pages_crawled < 15:
        for i in seedList:
            temp_links = getLinks(i)
            for j in range(len(temp_links)):
                if temp_links[j] not in new_links:
                    new_links.append(temp_links[j])
        seedList = new_links
        pages_crawled = len(new_links)
    '''

    for i in seedList:
        temp_links = getLinks(i)
        for j in range(len(temp_links)):
            if temp_links[j] not in new_links:
                new_links.append(temp_links[j])
        seedList = new_links
                
   # print(new_links)
        
    inverted_index = {}
    
    doc_id = 0
    for s in new_links:
        freq_dic = ourCrawler(s)
        for k in freq_dic.keys():
            v = freq_dic[k]
            if k not in inverted_index.keys():
                inverted_index[k] = [(doc_id, v)]
            else:
                inverted_index[k].append((doc_id, v))        
        doc_id += 1
     
    # sorted(inverted_index.keys())
   
    # print(inverted_index)
   
    writeURL(new_links)
    
    writeIndex(inverted_index)

    f = open("index.txt", "r+")
    tmp = f.readline()
    f.close()
    
    
    searchDoc(tmp)

    # query process
'''
    while True:
        query = input("Enter search query: ")
        query = query.lower()

        tokenizer = RegexpTokenizer(r'\w+')
        terms = tokenizer.tokenize(query)

        new_query = []

        for w in terms:
            w = porter.stem(w)
            new_query.append(w)

        boolTerm = new_query[1]
        search1 = new_query[0]
        search2 = new_query[2]

'''
        # if boolTerm == 'and' (i.e. base case)
        

if __name__== "__main__":
  main()
