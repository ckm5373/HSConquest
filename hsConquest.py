from csvMethods import getWinrate
import random
from simulation import runSimulation

def main():
    n = 0
    wins = 0
    while n < 100000:
        if runSimulation("EvenWarlock", "BigDruid", "OddRogue", "ZooWarlock", "EvenShaman", "TokenDruid") == 1:
            wins = wins + 1
        n = n + 1
    print("Player1's winrate is")
    print(wins / 100000)

if __name__ == "__main__": main()