import csv

def getWinrate(deck1, deck2):
    with open('winrates.csv') as winrates:
        data = list(csv.reader(winrates))
        decks  = data[0]
        deck1Index = decks.index(deck1)
        deck2Index = decks.index(deck2)
        return data[deck1Index][deck2Index]