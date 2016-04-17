#magic
##High Frequency Trading for Magic: The Gathering cards.



## Inspiration
We noticed that some of the prices for Magic: The Gathering card prices tend to react to "market news" at a relatively slow rate. A professional player would play the card, the card would increase in popularity in a short amount of time, but prices of the card would take a week to increase due to slow market response.

We wanted to take advantage of this opportunity to be market makers and buy up the cards before they increase in price, so that we can potentially make a tidy profit.

## What it does
This program seives through the over 28,000 Magic: The Gathering cards to determine candidates that will probably increase in price significantly in the near future.

It does this by getting rid of every potential card that may decrease in price by using several metrics (e.g. the card going out of rotation for the Standard format or the card is currently banned),
and then out of the remaining cards, will pick the ones that have seen a very recent spike in interest by the public using Google Trends.


## How we built it

###GETTING CARDS:

(each file in this section outputs a .txt file with the corresponding name)

listOfCards.py - gets list of all cards

listFutureOOR.py - list of cards going out of rotation within 2? months

ListOneWord.py - list of one word cards

listBanned.py - list of CURRENT banned cards


listFinal.txt - would contain final list of cards to potentially purchase


###GOOGLE TRENDS:
googleTrends.py - download the csv files for each card in list final

trendsAnalyzer.py - analyze the trends, outputs viable cards

###Main

main.py - this file combines all the above files into one easy to run program

## Challenges we ran into
Getting the list of every card (over 28,000!!!) was very difficult.

Google Trends "API" was difficult to work with.


## Accomplishments that we're proud of
We are most proud of how we integrating many different APIs (Google Trends), libraries (beautiful soup), and programs (the Magic master card list getter) together to form one coherent whole.

## What's next for magic
Backtesting the program, using better analysis, and perhaps eventually starting a small fund!
