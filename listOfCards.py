import itertools
import sys
import csv

def main():
    # sets field size to max to avoid memory overflow issues
    csv.field_size_limit(sys.maxsize)
    # opens file to write to
    with open('listOfCards.txt', 'w') as txtfile:
        # opens file to read from
        with open('listOfCards.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
            # iterates through lines of csv file to get names of cards
            for row in itertools.islice(reader, 1, 28370):
                # filters out non-alphabetic and non-space characters
                a = ''.join(filter((lambda x: (str.isalpha(x) or x==' ')), row[0]))
                txtfile.write("%s\n" % a)




