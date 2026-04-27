PlayerName = ""
MilesLeft = 2287.8
car = ""

cars = {
    "Honda civic" : {
        "Type": "Gasoline",
        "Mileage" : 49,
        "Full Tank" : 12.4,
        "Description" : "A standard car with a reliable mileage, not very green."
    },
    "Tesla Model 3" : {
        "Type" : "Electric",
        "Mileage" : 3.8,
        "Full Tank" : 70,
        "Description" : "An everyday electric car that is fairly easy to charge"
    },
    "Advanced Electric Car" : {
        "Type" : "Electric",
        "Mileage" : 3,
        "Full Tank" : 70,
        "Description" : "An electric vehicle that screams clean energy, difficult to charge."
    }
}
places = {
    "Chicago" : {
        "State" : "IL",
        "Next" : "Springfield",
        "Miles To Next" : 211
    },
    "Springfield" : {
        "State" : "IL",
        "Next" : "St. Louis",
        "Miles To Next" : 97.8
    },
    "St. Louis" : {
        "State" : "MO",
        "Next" : "Joplin",
        "Miles To Next" : 284
    },
    "Joplin" : {
        "State" : "MO",
        "Next" : "Oklahoma City",
        "Miles To Next" : 221
    },
    "Oklahoma City" : {
        "State" : "OK",
        "Next" : "Amarillo",
        "Miles To Next" : 258
    },
    "Amarillo" : {
        "State" : "TX",
        "Next" : "Santa Fe",
        "Miles To Next" : 290
    },
    "Santa Fe" : {
        "State" : "NM",
        "Next" : "Winslow",
        "Miles To Next" : 325
    },
    "Winslow" : {
        "State" : "AZ",
        "Next" : "Seligman",
        "Miles To Next" : 133
    },
    "Seligman" : {
        "State" : "AZ",
        "Next" : "Amboy",
        "Miles To Next" : 259
    },
    "Amboy" : {
        "State" : "CA",
        "Next" : "Santa Monica",
        "Miles To Next" : 209
    },
    "Santa Monica, Los Angeles" : {
        "State" : "CA",
        "Next" : "END",
        "Miles To Next" : "END"
    }
}