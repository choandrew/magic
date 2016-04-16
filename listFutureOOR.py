#! /usr/bin/env python3.5
#set information taken from http://mtgsalvation.gamepedia.com/Set
from bs4 import BeautifulSoup
import requests

#finds html of table of expansion sets
wiki = "http://mtgsalvation.gamepedia.com/Set"
r = requests.get(wiki)
html=r.content
soup = BeautifulSoup(html, "html.parser")#, "lxml")
table = soup.find("table",{"class":"wikitable sortable mw-collapsible"})
print (table)

#filter for "Expansion set"
#find first date > now date
#find expansion
f = open('listFutureOOR.csv', 'w')
count = 0
for row in table.findAll("tr"):
	cells = row.findAll("td")
	if len(cells) == 6:
		count=count+1
print (count)
	#for each "tr", assign each row to a variable