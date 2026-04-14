import time as mrgrauesclock
import Data
import GameLogic

def Display_Menu():
    print("Welcome to The Road To LA!")
    print("\nYou can: ")
    print("   1. Play Game\n   2. Options\n   3. Exit Game")
    return input("\nWhat do you wish to do? ")

def Clear_Screen():
    print("\n" * 50)

def Options():
    Clear_Screen()
    print("There are no options nerd...")
    if input("Press enter to go back ") == "Chicken":
        print("A mysterious power blesses you")
        mrgrauesclock.sleep(2)

playgame = False
while True:
    while playgame != True:
        Clear_Screen()
        choice = Display_Menu()
        if choice == "1":
            playgame = True
        elif choice == "2":
            Options()
        elif choice == "3":
            playgame = True
    if choice == "3":
        break
    Clear_Screen()
    Data.PlayerName = input("What should we name you, traveler? ")
    Clear_Screen()
    print("Let's start the game")
    mrgrauesclock.sleep(.65)
    Clear_Screen()
    print("Let's start the game.")
    mrgrauesclock.sleep(.65)
    Clear_Screen()
    print("Let's start the game..")
    mrgrauesclock.sleep(.65)
    Clear_Screen()
    print("Let's start the game...")
    mrgrauesclock.sleep(2)

    GameLogic.playgame()
    playgame = False
    