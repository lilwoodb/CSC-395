
import requests
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer

porter = PorterStemmer()

index = {}

def addIndex(url, parsedList):
    index[url] = parsedList
    return 

addIndex("http://hello.com", {'hi':3, 'lol':1})
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

# f.write('#eof') - Find a way to signify the end of a file 
f.close()

print(index)


# Search the Index

file = open("index.txt", "r")

query = "hi not lol"
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

results = []
currentUrl = ''
line = ''
url = 'http://'
url2 = 'https://'

def newline ():
    line = file.readline()
    currentLine = tokenizer.tokenize(line)
    return currentLine

if boolTerm == 'not':
    #pseudo: iterative loop to search index for search1
    #while (line == f.readline()) != '#eof':
    line = file.readline()
    for lines in file: 
        if url or url2 in line:
          currentUrl = line
          line = file.readline()
         # currentLine = newline()

          while url or url2 not in line: 
              if currentLine[0] == search1:
                  results.append(currentUrl)
                  currentLine = newline()
                  print('current results:', results)
              if currentLine[0] == search2:
                  if currentUrl in results:
                      results.remove(currentUrl)
                      print('removed old url')
                  
    
   # f.close()
#print(line)
if boolTerm == 'or':
    #pseudo: iterative loop with 'if' for search1, 'else-if' for search2
    print(search1, ' + ', search2)
if boolTerm == 'and':
    #pseudo: iterative loop to search index for search1 and 2
    print(search1, ' & ', search2)

f.close()
