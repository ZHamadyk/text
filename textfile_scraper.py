#!/bin/sh

#  textFile_scarper.py
#  
#
#  Created by Hamadyk on 2/8/16.
#
#import sys
#reload(sys)
#sys.setdefaultencoding('Cp1252')

from bs4 import BeautifulSoup as BS
import urllib

import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk.collocations
from nltk.corpus import stopwords

from collections import Counter

import re


input = raw_input("Enter Text File Name: ")
r = open(input).read()
# create a soup that
soup = BS(r).body.get_text()
#print soup

def space():
	print
	print

body_tokens = nltk.word_tokenize(soup)
#body_tokens = str(body_tokens)
body_text = nltk.Text(body_tokens)
body_text.collocations(num=50)



# finding the 20 most common words

stopwords = nltk.corpus.stopwords.words('english')
common_text = [w for w in body_text if w.lower() not in stopwords]
common_text = str(common_text)


common_search = re.findall('\w+', common_text.lower())
most_common = Counter(common_search).most_common(20)
print "build"
common_list = [w for w in most_common]
for i in common_list:
    print i


# allows you to search concordance of individual words
def leg_concordance():
	"""find concordance of input search term"""
	while True:
		search = raw_input("Enter search term: ")
		if search == "Done":
			break
		else:
			body_text.concordance(search)
			space()


# see how a term or phrase occurs within a larger context

soupSents = sent_tokenize(soup)
soupText = nltk.Text(soupSents)
def word_search():
    """Returns context in which search term occurs"""
    while True:
        search = raw_input("Enter word or phrase to locate: ")
        if search == "Done":
            print "Return to concordance searching or exit? y to return; e to exit"
            answer = raw_input("> ")
            if answer == "y":
                return leg_concordance()
            else: break
        
        else:
            word_find = [w for w in soupText if search in w] 
            for line in word_find:
                print line
                space()
        space()
        print "End of search for '{}'.".format(search)
        print "________________________________________"
        space()
    

shall_count = body_text.count('shall')
must_count = body_text.count('must')
may_count = body_text.count('may')

space()

print "'shall' occurs {} times in this text.".format(shall_count)
print "Remember 'shall' requires some action be taken, expresses a prediction or intention."
space()
print "'must' occurs {} times in this text.".format(must_count)
print "Use of 'must' creates ambiguity; the word implies more obligation than command. However the Fed manual says to use 'must' instead of 'shall'"
space()
print "'may' occurs {} times in this text.".format(may_count)
print "Using 'may' can express capability or possibility as well as authoirty."
space()

print "Lets do some basic search of this text!"
leg_concordance()
space()
word_search()
space()

