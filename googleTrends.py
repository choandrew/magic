from pytrends.pyGTrends import pyGTrends
import time
from random import randint
import glob, os

def main():
    googleUsername = "basedgodkiller@gmail.com"
    googlePassword = "Unicorn7!"
    
    #connect to Google
    connector = pyGTrends(googleUsername, googlePassword)
    
    with open("listFinal.txt", "r") as f:
        
        #creates array each containing a card name as a string
        cards = [line.rstrip('\n') for line in f]
        
        for card in cards:
            connector.request_report(card,geo="US", date="today 90-d")
            connector.save_csv("./output/", card)
            
            #so that google trends doesn't get suspicious of scripting...
            time.sleep(randint(4,8))


    path = "./output"

    os.chdir(path)

    for file in glob.glob("*.csv"):
        
        f = open(file,"r")
        
        lines = f.readlines()
        f.close()

        del(lines[0:5])
        lines = lines[0:90]

        f = open(file,"w")

        for line in lines:
            f.write(line)







if __name__ == "__main__":
    main()
