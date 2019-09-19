
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
stop_words = set(stopwords.words('english'))
#from nltk.tokenize import word_tokenize

porter = PorterStemmer()
#page = requests.get("https://en.wikipedia.org/wiki/Magliocca")

def ourCrawler(url):
    
    page = requests.get(url)
    print(page)
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

        
    #print(word_list)
    return word_list


def main():
    seedList = ["https://en.wikipedia.org/wiki/Magliocca", "https://en.wikipedia.org/wiki/Puppy"]

    inverted_index = {}
    doc_id = 0
    for s in seedList:
        freq_dic = ourCrawler(s)
       # print(type(freq_dic))
        for k in freq_dic.keys():
            v = freq_dic[k]
            if k not in inverted_index.keys():
                inverted_index[k] = [(doc_id, v)]
            else:
                inverted_index[k].append((doc_id, v))
        doc_id += 1

    sorted(inverted_index.keys())

    print(inverted_index)




if __name__== "__main__":
  main()
