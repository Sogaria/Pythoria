
coffeeMachineOn = True

coffeeRessources = {
    "Water" : 1000,
    "Milk"  : 500,
    "Coffee": 100,
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

coffeeDict = {
    "espresso"  : espressoStats,
    "latte"     : latteStats,
    "cappuccino": cappuccinoStats
}

def PrintReport():
    print(f"Water: {coffeeRessources["Water"]}ml")      
    print(f"Milk: {coffeeRessources["Milk"]}ml")
    print(f"Coffee: {coffeeRessources["Coffee"]}g")
    print(f"Water: ${coffeeRessources["Money"]}")

def RessourceCheck(coffeeType: str) -> bool:
    ressourcesEnough = True
    coffeeStats = coffeeDict.get(coffeeType) #access value (dictionary of specific coffee stats)
    for key in coffeeRessources:
        if coffeeRessources[key] == "Money":
            continue
        if coffeeRessources[key] < coffeeStats[key]:
            print(f"Sorry there is not enough {key.lower()}.")
            ressourcesEnough = False
    if ressourcesEnough:
        ConsumeRessources(coffeeStats)
        print(f"Your {coffeeType} will be served soon. Please insert ${coffeeStats["Money"]} in coins.")

def ConsumeRessources(coffeeType: dict):
    for key in coffeeRessources:
        if key == "Money":
            continue
        else:
            coffeeRessources[key] -= coffeeType[key]

while coffeeMachineOn == True:
    prompt = input("What would you like? (espresso/latte/cappuccino) ")
    if prompt == "off":
        coffeeMachineOn == False
        break
    elif prompt == "print":
        PrintReport()
    else:
        RessourceCheck(prompt)
