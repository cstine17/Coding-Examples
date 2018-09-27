
# coding: utf-8

# In[1]:


#goal is as follows: would you be able to write a Python script to scrape this article we wrote. 
#https://medium.com/aequicens/https-medium-com-aequicens-why-artificial-intelligence-isnt-intelligent-yet-644b8ae8ff95 
#We simply want a list with each paragraph as its own string.
#We also want a list of lists where each paragraph is a list of tokens processed using ntlk tokenizer.
#Just send the script attached to an email, and also please ask any questions.


#Importing packages
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer

#Using requests to import html
mediumUrl = "https://medium.com/aequicens/https-medium-com-aequicens-why-artificial-intelligence-isnt-intelligent-yet-644b8ae8ff95"
rMedium = requests.get(mediumUrl)
mediumHtml = rMedium.text
#print(mediumHtml)

#Use BeautifulSoup to create 'beautifulsoup' object from html
mediumSoup = BeautifulSoup(mediumHtml, "html5lib")

#use beautifulsoup to create a ResultSet
mediumResultSet = mediumSoup.find_all('p')

#create list to store values then iterate through resultset to append text to list
listOfParagraphStrings = []
for i in mediumResultSet:
    listOfParagraphStrings.append(i.text)

#Initially, I took the goal literally and took out any objects marked as paragraphs within the html code
#This has left a run of 'quasi paragraphs' at the end, which I remove manually before printing my list of paragraphs 
del listOfParagraphStrings[10:21]

#Output produces 1st Goal "We simply want a list with each paragraph as its own string."
print(listOfParagraphStrings)

#creating tokenizer
tokenMachine = RegexpTokenizer('\w+')

#create empty list to place tokenized paragraphs
listOfTokenLists = []
for j in listOfParagraphStrings:
    listOfTokenLists.append(tokenMachine.tokenize(j))

#Output produces 2nd goal "We also want a list of lists where each paragraph is a list of tokens processed using ntlk tokenizer."
print(listOfTokenLists)

