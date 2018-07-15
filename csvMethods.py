import csv

def getDeckIndex(deck):
    with open('winrates.csv') as winrates:
        data = list(csv.reader(winrates))
        decks = data[0]
        return decks.index(deck)

def getWinrate(deck1, deck2):
    with open('winrates.csv') as winrates:
        data = list(csv.reader(winrates))
        decks  = data[0]
        return data[deck1][deck2]