import random as mrgraue
import time as mrgrauesclock
import Data

def Clear_Screen():
    print("\n" * 50)

def DisplayLocation():
    print("You have left {}, {}".format(Data.places[Data.location]["Name"], Data.places[Data.location]["State"]))
    print("You have {} miles left untill {}, {}".format(Data.places[Data.location]["Miles To Next"] - Data.MilesDrivenUntillNext,Data.places[Data.location+1]["Name"], Data.places[Data.location+1]["State"]))
    print("You are {} miles away from Santa Monica, Los Angeles, CA".format(Data.MilesLeft - Data.MilesDriven))

    print("\nYou are driving a {}, you have {} miles left untill it's empty".format(Data.car, Data.TankLeft * Data.cars[Data.car]["Mileage"]))

def playgame():
    print("A world where nobody cares for their environment")
    print("You are determined to change humanity...")
    
    mrgrauesclock.sleep(4)
    Clear_Screen()

    print("You decide to step up by tackling a journey from Chicago to Los Angeles with little to no carbon emmisions")
    input("\nIt's time to choose how you are going to approach this journey [press enter]")

    Clear_Screen()

    print("Traveling on route 66 to Los Angeles isn't easy,\nso you will need a reliable car that is also going to promote green energy")
    mrgrauesclock.sleep(2)

    input("Chose what car you will take on the way [press enter]")
    
    Clear_Screen()

    print("Honda Civic:\n   Type: {}\n   Mileage: {}\n   Tank Capacity: {}\n   {}".format(Data.cars["Honda civic"]["Type"],Data.cars["Honda civic"]["Mileage"],Data.cars["Honda civic"]["Full Tank"],Data.cars["Honda civic"]["Description"]))
    input("[press enter]")

    Clear_Screen()

    print("Tesla Model 3:\n   Type: {}\n   Mileage: {}\n   Tank Capacity: {}\n   {}".format(Data.cars["Tesla Model 3"]["Type"],Data.cars["Tesla Model 3"]["Mileage"],Data.cars["Tesla Model 3"]["Full Tank"],Data.cars["Tesla Model 3"]["Description"]))
    input("[press enter]")

    Clear_Screen()

    print("Advanced Electric Car:\n   Type: {}\n   Mileage: {}\n   Tank Capacity: {}\n   {}".format(Data.cars["Advanced Electric Car"]["Type"],Data.cars["Advanced Electric Car"]["Mileage"],Data.cars["Advanced Electric Car"]["Full Tank"],Data.cars["Advanced Electric Car"]["Description"]))
    input("[press enter]")

    Clear_Screen()

    while True:
        input1 = input("What do you wish to choose?\n   1. Honda Civic\n   2. Tesla Model 3\n   3. Advanced Electric Car")
        if input1 == "1":
            Data.car = "Honda civic"
            break
        elif input1 == "2":
            Data.car == "Tesla Model 3"
            break
        elif input1 == "3":
            Data.car = "Advanced Electric Car"
            break
        else:
            input("You did not input a correct value [press enter]")
            Clear_Screen()

    Data.TankLeft = Data.cars[Data.car]["Full Tank"]

    Clear_Screen()

    print("Nice Choice! Now let's start the game!!!")

    mrgrauesclock.sleep(2)
    Clear_Screen()

    print("You decide to depart from Chicago on on November 5th, your goal is to make it to Santa Monica, Los Angeles")
    input("[press enter]")

    Clear_Screen()

    DisplayLocation()