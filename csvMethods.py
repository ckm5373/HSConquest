import csv, random

def getDeckIndex(deck):
    with open('winrates.csv') as winrates:
        data = list(csv.reader(winrates))
        decks = data[0]
        return decks.index(deck)

def getRandomLineup():
    with open('winrates.csv') as winrates:
        data = list(csv.reader(winrates))
        decks = data[0]
        decks.remove("Blank")
        deck1 = random.choice(decks)
        decks = trimDecklists(decks, deck1)
        deck2 = random.choice(decks)
        decks = trimDecklists(decks, deck2)
        deck3 = random.choice(decks)
        return [deck1, deck2, deck3]

def getWinrate(deck1, deck2):
    with open('winrates.csv') as winrates:
        data = list(csv.reader(winrates))
        return data[deck1][deck2]

def trimDecklists(decks, pickedDeck):
    if "Druid" in pickedDeck:
        decks = [x for x in decks if "Druid" not in x]
    elif "Hunter" in pickedDeck:
        decks = [x for x in decks if "Hunter" not in x]
    elif "Mage" in pickedDeck:
        decks = [x for x in decks if "Mage" not in x]
    elif "Paladin" in pickedDeck:
        decks = [x for x in decks if "Paladin" not in x]
    elif "Priest" in pickedDeck:
        decks = [x for x in decks if "Priest" not in x]
    elif "Rogue" in pickedDeck:
        decks = [x for x in decks if "Rogue" not in x]
    elif "Shaman" in pickedDeck:
        decks = [x for x in decks if "Shaman" not in x]
    elif "Warlock" in pickedDeck:
        decks = [x for x in decks if "Warlock" not in x]
    elif "Warrior" in pickedDeck:
        decks = [x for x in decks if "Warrior" not in x]
    return decks