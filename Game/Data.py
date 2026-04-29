PlayerName = ""
MilesLeft = 2287.8
car = ""
location = 1
MilesDriven = 0
MilesDrivenUntillNext = 0
TankLeft = 0
CarbonEmissions = 0
play = True

cars = {
    "Honda civic" : {
        "Type": "Gasoline",
        "Mileage" : 49,
        "Full Tank" : 12.4,
        "Description" : "A standard car with a reliable mileage, not very green.",
        "Fuel Chance" : 3
    },
    "Tesla Model 3" : {
        "Type" : "Electric",
        "Mileage" : 3.8,
        "Full Tank" : 70,
        "Description" : "An everyday electric car that is fairly easy to charge",
        "Fuel Chance" : 5
    },
    "Advanced Electric Car" : {
        "Type" : "Electric",
        "Mileage" : 3,
        "Full Tank" : 70,
        "Description" : "An electric vehicle that screams clean energy, difficult to charge.",
        "Fuel Chance" : 10
    }
}
places = {
    1 : {
        "Name" : "Chicago",
        "State" : "IL",
        "Next" : "Springfield",
        "Miles To Next" : 211
    },
    2 : {
        "Name" : "Springfield",
        "State" : "IL",
        "Next" : "St. Louis",
        "Miles To Next" : 97.8
    },
    3 : {
        "Name" : "St. Louis",
        "State" : "MO",
        "Next" : "Joplin",
        "Miles To Next" : 284
    },
    4 : {
        "Name" : "Joplin",
        "State" : "MO",
        "Next" : "Oklahoma City",
        "Miles To Next" : 221
    },
    5 : {
        "Name" : "Oklahoma City",
        "State" : "OK",
        "Next" : "Amarillo",
        "Miles To Next" : 258
    },
    6 : {
        "Name" : "Amarillo",
        "State" : "TX",
        "Next" : "Santa Fe",
        "Miles To Next" : 290
    },
    7 : {
        "Name" : "Santa Fe",
        "State" : "NM",
        "Next" : "Winslow",
        "Miles To Next" : 325
    },
    8 : {
        "Name" : "Winslow",
        "State" : "AZ",
        "Next" : "Seligman",
        "Miles To Next" : 133
    },
    9 : {
        "Name" : "Seligman",
        "State" : "AZ",
        "Next" : "Amboy",
        "Miles To Next" : 259
    },
    10 : {
        "Name" : "Amboy",
        "State" : "CA",
        "Next" : "Santa Monica",
        "Miles To Next" : 209
    },
    11 : {
        "Name" : "Santa Monica, Los Angeles",
        "State" : "CA",
        "Next" : "END",
        "Miles To Next" : 0
    }
}