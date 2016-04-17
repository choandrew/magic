#! /usr/bin/env python3.5
#set information taken from http://mtgsalvation.gamepedia.com/Set
from bs4 import BeautifulSoup
import requests
import time

def removeTag(string):
	nohead = (string.split("<td> "))[1]
	notail = (nohead.split(" </td>"))[0]
	return notail

def stringToDate(string):
	string = removeTag(string)
	ym = string.split('-')
	year = int(ym[0])
	month = int(ym[1])
	return [year, month]
#finds html of table of expansion sets
wiki = "http://mtgsalvation.gamepedia.com/Set"
r = requests.get(wiki)
html=r.content
soup = BeautifulSoup(html, "html.parser")#, "lxml")
table = soup.find("table",{"class":"wikitable sortable mw-collapsible"})
#print (table)

#filter for "Expansion set"
#find first date > now date
#find expansion
f = open('listFutureOOR.csv', 'w')
count = 0
cmonth = int(time.strftime("%m"))
cyear = int(time.strftime("%Y"))
for row in table.findAll("tr"):
	cells = row.findAll("td")
	print(len(cells))
	if len(cells) ==2:
		print (cells[0])
		print(cells[1])
	if len(cells) == 6:
		date = stringToDate(str(cells[0]))
		name = cells[1]
		typeSet = cells[4]
		print (date[0], date[1])
		count=count+1
		if date[0] >= cyear:
			print("relevaant")
		else:
			print ("hi")
print (count)
	#for each "tr", assign each row to a variable
