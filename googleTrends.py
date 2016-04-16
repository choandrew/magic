import pytrends


with open("listFinal.txt", "r") as f:
    cards = [line.rstrip('\n') for line in open('filename')]
    
    for card in cards:
        csv = pytrends.request_report(keywords, hl=card, cat=None, geo="US", date=None, gprop=None)
        pytrends.save_csv("./output", card)

