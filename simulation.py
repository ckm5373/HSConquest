import random
from csvMethods import getDeckIndex, getWinrate, getRandomLineup

def runSimulation(deck1, deck2, deck3, deck4, deck5, deck6):
    deck1Index = getDeckIndex(deck1)
    deck2Index = getDeckIndex(deck2)
    deck3Index = getDeckIndex(deck3)
    deck4Index = getDeckIndex(deck4)
    deck5Index = getDeckIndex(deck5)
    deck6Index = getDeckIndex(deck6)

    player1Decks = [deck1Index, deck2Index, deck3Index]
    player2Decks = [deck4Index, deck5Index, deck6Index]
    
    while len(player1Decks) > 0 and len(player2Decks) > 0:
        player1Choice = random.choice(player1Decks)
        player2Choice = random.choice(player2Decks)
        player1Winrate = getWinrate(player1Choice, player2Choice)

        if random.random() < (float(player1Winrate) * 0.01):
            player1Decks.remove(player1Choice)
        else:
            player2Decks.remove(player2Choice)

    if len(player1Decks) == 0:
        #print("Player1 wins vs " + deck4 + ", " + deck5 + ", " + deck6)
        return 1
    elif len(player2Decks) == 0:
        #print("Player1 loses vs " + deck4 + ", " + deck5 + ", " + deck6)
        return 2
    else:
        print("somehow nobody won")
        return 0

def runSimulationMultiple(deck1, deck2, deck3, deck4, deck5, deck6, sets):
    n = 0
    wins = 0
    while n < sets:
        if runSimulation(deck1, deck2, deck3, deck4, deck5, deck6) == 1:
            wins = wins + 1
        n = n + 1
    return 100 * wins / sets

def runSimulationVsAll(deck1, deck2, deck3, sets):
    n = 0
    wins = 0
    while n < sets:
        opponentDecks = getRandomLineup()
        if runSimulation(deck1, deck2, deck3, opponentDecks[0], opponentDecks[1], opponentDecks[2]) == 1:
            wins = wins + 1
        n = n + 1
    return 100 * wins / sets