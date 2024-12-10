
coffeeMachineOn = True

coffeeRessources = {
    "Water" : 1000,
    "Milk"  : 500,
    "Coffee": 200,
    "Money" : 5
}

espressoStats = {
    "Water" : 150,
    "Milk"  : 50,
    "Coffee": 20,
    "Money" : 2
}

latteStats = {
    "Water" : 250,
    "Milk"  : 200,
    "Coffee": 25,
    "Money" : 3.5
}

cappuccinoStats = {
    "Water" : 200,
    "Milk"  : 150,
    "Coffee": 27,
    "Money" : 3.5
}

def PrintReport():
    print(f"Water: {coffeeRessources["Water"]}ml")
    print(f"Milk: {coffeeRessources["Milk"]}ml")
    print(f"Coffee: {coffeeRessources["Coffee"]}g")
    print(f"Water: ${coffeeRessources["Money"]}")


while coffeeMachineOn == True:
    prompt = input("What would you like? (expresso/latte/cappuccino) ")
    if prompt == "off":
        coffeeMachineOn == False
        break
    elif prompt == "print":
        PrintReport()

