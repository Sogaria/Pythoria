
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
        print(f"Your {coffeeType} will be served soon. It costs ${coffeeStats["Money"]}.")

def ConsumeRessources(coffeeType: dict):
    for key in coffeeRessources:
        if key == "Money":
            continue
        else:
            coffeeRessources[key] -= coffeeType[key]

def ServeCoffee(coffee: str, leftToPay: float, price: float):
    if leftToPay == 0:
        print(f"Thanks! Enjoy your {coffee}!")
    if leftToPay < 0:
        exchange = leftToPay * -1
        if exchange <= coffeeRessources["Money"]:
            coffeeRessources["Money"] -= exchange
            print(f"Here is your ${exchange} exchange. And enjoy your {coffee} :)")
        elif exchange > coffeeRessources["Money"]:
            print("Sadly we do not have enough exchange, sorry. Please take your refund.")

while coffeeMachineOn == True:
    prompt = input("What would you like? (espresso/latte/cappuccino) ")
    if prompt == "off":
        coffeeMachineOn == False
        break
    elif prompt == "print":
        PrintReport()
    else:
        RessourceCheck(prompt)
    #coins insertion
    coin_Inserted = 0
    coffeeStats = coffeeDict.get(prompt)
    leftToPay = coffeeStats["Money"]
    while coin_Inserted < coffeeStats["Money"]:
        coin = float(input("Please insert coins now to pay ($0.01, $0.05, $0.1, $0.25): $"))
        leftToPay -= coin
        coin_Inserted += coin
        if leftToPay <= 0:
            ServeCoffee(prompt, leftToPay, coffeeStats["Money"])
        else:
            print(f"${leftToPay} left to pay! ")

