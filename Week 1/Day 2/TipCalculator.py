def tipCalc ():
    print("Welcome to the tip calculator!")
    totalBill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
    split = int(input("How many people to split the bill?"))
    costPerPerson = (totalBill+tip) / split
    costPerPerson = round(costPerPerson, 2)
    print(f"Each person should pay: ${costPerPerson}")

tipCalc()

