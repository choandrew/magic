
#set information taken from http://mtgsalvation.gamepedia.com/Set
from bs4 import BeautifulSoup
import requests
import csv
 

from datetime import datetime
def dateParse(mdy):
	sp = mdy.split(' ')
	if len(sp) ==3:
		if mdy[0] == "c":
			if (sp[1] == "Spring") | (sp[1]=="Fall") | (sp[1] == "Winter") | (sp[1] =="Summer"):
				date =datetime.strptime(sp[2], '%Y')
			else: 
				mdy = mdy[3:]
				date = datetime.strptime(mdy, '%B %Y')
		else:
			date = datetime.strptime(mdy, '%B %d, %Y')
		#month = mdy[0]
		#day = mdy[1]
		#year = mdy[2]

	if len(sp) ==2:
		if (sp[0] == "Spring") | (sp[0]=="Fall") | (sp[0] == "Winter") | (sp[0] =="Summer"):
			date.time.strptime(sp[1], '%Y')
		else:
			date = datetime.strptime(mdy, '%B %Y')
	return date
		#mont = mdy[0]
		#day = 1
		#year = mdy[1]
	#year = int(ym[0])
	#month = int(ym[1])
	#return [year, month]
def main():
	#finds html of table of expansion sets
	wiki = "https://en.wikipedia.org/wiki/List_of_Magic:_The_Gathering_sets"
	r = requests.get(wiki)
	html=r.content
	soup = BeautifulSoup(html, "html.parser")#, "lxml")
	table = soup.find("table",{"style":"font-size:95%;"})
	soup = BeautifulSoup(str(table), "html.parser")

	count = 0
	today = datetime.now()
	rows = soup.find_all('tr')
	listrec = []
	for row in rows:
		soup = BeautifulSoup(str(row), "html.parser")
		cells = soup.find_all('td')
		if len(cells) >=7:
			date =dateParse((cells[5].contents)[0])
			name =cells[0].string
			abbr = ((cells[2].contents)[0])
			if date >= today:
				inPlay = listrec[(len(listrec)-4):]
				compareSet(inPlay)
				return
			if date.year >= int(today.year) -1:
				listrec.append(abbr)
def compareSet(inPlay):
	f = open('listOfCardsSets.txt', 'rt',encoding='iso-8859-15')
	g = open('listFutureOOR.txt', 'wt',encoding='iso-8859-15')
	try: 
		writer =csv.writer(g)
		reader = csv.reader(f)
		for row in reader:
			abbrev = row[1][1:]
			if abbrev in inPlay:
				writer.writerow([row[0]])
	finally: 
		g.close()
		f.close()
	return



if __name__ == "__main__":
    main()
