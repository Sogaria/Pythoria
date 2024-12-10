size = input("S, M or L: ")
pepperoni = input("Pepperoni? Y or N: ")
extra_cheese = input("Extra cheese? Y or N: ")

totalcost = 0
if size == "S": totalcost += 15
elif size == "M": totalcost += 20
elif size == "L": totalcost += 25

if pepperoni == "Y": totalcost += 2
if extra_cheese == "Y": totalcost += 2

print("That would be", totalcost, "€!")
