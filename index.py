# https://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python


import requests
import nltk
from nltk.corpus import wordnet as wn

index = {}

def addIndex(url, parsedList):
    index[url] = parsedList
    return 

addIndex("http://hello.com", {'hi':3})
addIndex("http://google.com", {'you':4, 'we':1})
addIndex("http://iwannadie.lol", {'lol':9, 'kmp':2})

f = open("index.txt", "w+")

for x in index:
    f.write(x)
    f.write('\n')
    for y in index[x]:
        f.write(y)
        f.write(' ')
        f.write(str(index[x][y]))
        f.write('\n')
        
f.close()

print(index)



