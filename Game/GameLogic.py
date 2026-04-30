import random as mrgraue
import time as mrgrauesclock
import Data

def Clear_Screen():
    print("\n" * 50)

def Menu():
    while Data.play:
        Clear_Screen()
        DisplayLocation()
        print("\n What do you choose to do: \n   1. Travel on the road\n   2. Find somewhere to fuel")
        choice = input()
        if choice == "1":
            Travel()
        elif choice == "2":
            Fuel()
        else:
            print("Put in a valid value")
            mrgrauesclock.sleep(2)

def Travel():
    Clear_Screen()
    MilesDriven = mrgraue.randint(10, 60)
    input("You decide to travel {} miles [press enter]".format(MilesDriven))
    FuelUsed = MilesDriven / Data.cars[Data.car]["Mileage"]
    Data.TankLeft -= FuelUsed
    Data.MilesDrivenUntillNext += MilesDriven
    Data.MilesLeft -= MilesDriven
    if Data.places[Data.location]["Miles To Next"] - Data.MilesDrivenUntillNext <= 0:
        Data.MilesDrivenUntillNext = 0
        Data.location += 1
        print("You have arrived in {}, and completely refuel your vehicle".format(Data.places[Data.location]["Name"]))
        mrgrauesclock.sleep(2)
        Data.CarbonEmissions += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
        Data.TankLeft += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
        if Data.location == 11:
            Data.play = False
    if Data.TankLeft <= 0:
        print("You ran out of fuel, What do you wish to do?")
        choice = input("   1. Push your car to the nearest fuel station\n   2. attempt to crete natural fuel\n   3. Attempt to hitch a ride with a stranger")
        if choice == "1":
            fuel = mrgraue.randint(1, 10)
            if fuel == 1:
                print("You find a fuel station, and manage to fuel your car")
                Data.CarbonEmissions += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
                Data.TankLeft += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
            else:
                print("You cannot find a gas station and soon you die of starvation")
                Data.play = False
        elif choice == "2":
            fuel  = mrgraue.randint(1,4)
            if fuel == 1:
                print("You manage to create fuel by using natural gas created by the human body")
                Data.CarbonEmissions += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
                Data.TankLeft += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
            elif fuel == 2:
                print("You accidentaly create toxic gas and die")
                Data.play = False
            else:
                print("You fail to create gas. DONE")
                Data.play = False
        elif choice == "3":
            hitch = mrgraue.randint(1, 15)
            if hitch == 1:
                print("You hitch a ride and they take you all the way to Los Angeles")
                Data.play = False
            else:
                print("You cannot hitch a ride and die")
                Data.play = False
    mrgrauesclock.sleep(2)

        
def Fuel():
    fuelChance = mrgraue.randint(1, Data.cars[Data.car]["Fuel Chance"])
    if fuelChance == 1:
        print("You managed to find somewhere to replenish your vehicle's fuel and continue your journey")
        Data.CarbonEmissions += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
        Data.TankLeft += Data.cars[Data.car]["Full Tank"] - Data.TankLeft
    else:
        print("You could not find a place to fuel your vehicle, you decide to continue the drive")
    mrgrauesclock.sleep(2)
    Travel()

def DisplayLocation():
    print("You have left {}, {}".format(Data.places[Data.location]["Name"], Data.places[Data.location]["State"]))
    print("You have {} miles left untill {}, {}".format(Data.places[Data.location]["Miles To Next"] - Data.MilesDrivenUntillNext,Data.places[Data.location+1]["Name"], Data.places[Data.location+1]["State"]))
    # print("You are {} miles away from Santa Monica, Los Angeles, CA".format(Data.MilesLeft - Data.MilesDriven))

    print("\nYou are driving a {}, you have {} miles left untill it's empty".format(Data.car, Data.TankLeft * Data.cars[Data.car]["Mileage"]))

def playgame():
    Data.PlayerName = ""
    Data.MilesLeft = 2287.8
    Data.car = ""
    Data.location = 1
    Data.MilesDriven = 0
    Data.MilesDrivenUntillNext = 0
    Data.TankLeft = 0
    Data.CarbonEmissions = 0
    Data.play = True
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
        input1 = input("What do you wish to choose?\n   1. Honda Civic\n   2. Tesla Model 3\n   3. Advanced Electric Car\n")
        if input1 == "1":
            Data.car = "Honda civic"
            break
        elif input1 == "2":
            Data.car = "Tesla Model 3"
            break
        elif input1 == "3":
            Data.car = "Advanced Electric Car"
            break
        else:
            input("You did not input a correct value [press enter]")
            Clear_Screen()

    Data.TankLeft = Data.cars[Data.car]["Full Tank"]
    Data.CarbonEmissions = Data.TankLeft

    Clear_Screen()

    print("Nice Choice! Now let's start the game!!!")

    mrgrauesclock.sleep(2)
    Clear_Screen()

    print("You decide to depart from Chicago on on November 5th, your goal is to make it to Santa Monica, Los Angeles")
    input("[press enter]")

    Clear_Screen()
    Data.play = True
    while Data.play == True:
        if Data.play == False:
            break
        Menu()
    Clear_Screen()
    if(Data.location == 11):
        input("You Made IT! Now let's discuss your carbon emissions [press enter]")
    else:
        input("You did not make it to Los Angeles, but let's still talk about your carbon emissions [press enter]")
    if Data.car == "Honda civic":
        print("\nYou chose the Honda Civic to take on your journey, it was the only gas-powered vehicle offered to you")
        print("In the entirety of your trip you burned {} gallons of gas, that's not very green".format(Data.CarbonEmissions))
        print("In the lifetime of a Honda Civic, it releases 30 tons of CO2!!")
        print("As a society, we can do better by switching to a greener option\n\n")
        input("[press enter]")
    elif Data.car == "Tesla Model 3":
        print("\nYou chose the Tesla Model 3, a much greener option than the honda civic!")
        print("In the lifetime of a Tesla Model 3, it only releases around 16 tons of C02, 14 tons less than the Honda Civic")
        print("Even though it is a greener option than the Honda, it still releases CO2")
        print("As a society, we can do better by switching to a greener option\n\n")
        input("[press enter]")
    elif Data.car == "Advanced Electric Car":
        print("\nYou Chose the Advanced Electric Car, the greenest option available")
        print("While this car is fictional, our goal should be to create a greener car that only releases a few tons of C02 in it's entire lifetime")
        print("As a society, we can do better by switching to a greener option\n\n")
        input("[press enter]")
    Clear_Screen()