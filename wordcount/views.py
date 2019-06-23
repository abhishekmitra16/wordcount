from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(req):
    return render(req,'home.html')

def count(req):
    text = req.GET['fulltext']

    wordlist = text.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(req, 'count.html',{'fulltext':text, 'count': len(wordlist), 'sortedwords':sortedwords})

def about(r):
    return render(r, 'about.html')