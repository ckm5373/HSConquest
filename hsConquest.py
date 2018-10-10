from csvMethods import getWinrate, getRandomLineup
import random
from simulation import runSimulation, runSimulationMultiple, runSimulationVsAll

def main():
    highestWinrate = 0
    bestLineup = []
    n = 0
    #number of lineups to try
    while n < 500:
        lineup = getRandomLineup()
        #last number is number of random matchups to test lineup vs
        winrate = runSimulationVsAll(lineup[0], lineup[1], lineup[2], 10000)
        if winrate > highestWinrate:
            highestWinrate = winrate
            bestLineup = lineup
            print("New best lineup is: " + str(bestLineup) + " with a " + str(highestWinrate) + "% winrate.")
        else: 
            print("Lineup: " + str(lineup) + " doesn't make the cut with a " + str(winrate) + "% winrate.")
            print("Best lineup is still: " + str(bestLineup) + " with a " + str(highestWinrate) + "% winrate.")
        n = n + 1

if __name__ == "__main__": main()