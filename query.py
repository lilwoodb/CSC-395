import requests
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn

porter = PorterStemmer()

keywords = ["and","not","or"]

while True:
    query = input("Enter search query: ")
    query = query.lower()

    tokenizer = RegexpTokenizer(r'\w+')
    terms = tokenizer.tokenize(query)

    new_query = []

    for w in terms:
        w = porter.stem(w)
        new_query.append(w)

    old = ''
    current = ''
    future = ''

    AND = []
    NOT = []
    OR = []

    boolTerm = new_query[1]
    search1 = new_query[0]
    search2 = new_query[2]

    if boolTerm == 'not':
        #pseudo: iterative loop to search index for search1
        print(search1)
    if boolTerm == 'or':
        #pseudo: iterative loop with 'if' for search1, 'else-if' for search2
        print(search1, ' + ', search2)
    if boolTerm == 'and':
        #pseudo: iterative loop to search index for search1 and 2
        print(search1, ' & ', search2)

    ##for i in range(len(new_query)):
    ##    if i == 0:
    ##        old = new_query[0]
    ##        #current = new_query[1]
    ##    if i > 0:
    ##        current = new_query[i]
    ##        if new_query[i] == 'and':
    ##            AND.append[old]
    ##            old = current
    ##            current = future
    ##    if i+1 in range(len(new_query)):
    ##        future = new_query[1+i]
            
    print(new_query)
# end of while, continues to loop until terminated



### THINGS TO ADD TO README":
    # three words: term1, boolean, term2
    # search terms can't be words with spaces in them
    # only one boolean
    # only two search terms, both have to be nouns
