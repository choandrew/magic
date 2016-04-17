# magic

##High frequency trading for Magic: The Gathering cards.

This program seives through the over 28,000 Magic: The Gathering cards to determine candidates that will probably increase in price significantly in the near future.

It does this by getting rid of every potential card that may decrease in price by using several metrics (e.g. the card going out of rotation for the Standard format or the card is currently banned),
and then will


## FILE DESCRIPTION

main.py - list of cards that we will measure, basically combines all the above files




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


###Reasons why cards lose value:
Rotated out of standard (cards only played from latest 3 expansion blocks)
Shifting meta / decrease in relative strength
Banned
Times of volatility
Reprinting
