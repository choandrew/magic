# magic

##High Frequency Trading for Magic: The Gathering cards.

This program seives through the over 28,000 Magic: The Gathering cards to determine candidates that will probably increase in price significantly in the near future.

It does this by getting rid of every potential card that may decrease in price by using several metrics (e.g. the card going out of rotation for the Standard format or the card is currently banned),
and then out of the remaining cards, will pick the ones that have seen a very recent spike in interest by the public using Google Trends.


## FILE DESCRIPTION

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
