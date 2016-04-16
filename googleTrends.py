from pytrends.pyGTrends import pyGTrends
import time
from random import randint

def main():
    googleUsername = "basedgodkiller@gmail.com"
    googlePassword = "Unicorn7!"
    
    #connect to Google
    connector = pyGTrends(googleUsername, googlePassword)
    
    with open("listFinal.txt", "r") as f:
        cards = [line.rstrip('\n') for line in f]
        
        for card in cards:
            connector.request_report(card,geo="US", date="today 90-d")
            connector.save_csv("./output/", card)
            time.sleep(randint(4,8))


