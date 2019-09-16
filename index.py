

import requests
import nltk
from nltk.corpus import wordnet as wn

index = {}

def addIndex(url, parsedList):
    index[url] = parsedList
    return 



addIndex("http://hello.com", {'hi':3})
addIndex("http://google.com", {'you':4, 'we':1})

f = open("index.txt", "w+")

for key, value in index.items():
    f.write(key)
    f.write(value)

    
##for link in index:
##    url = 
##    f.write(index[link])
##    f.write(index.get(

    
f.close()
print(index)
