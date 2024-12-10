import os
def Addition(x: float, y: float) -> float:
    return x+y
def Subtract(x: float, y: float) -> float:
    return x-y
def Multiply(x: float, y: float) -> float:
    return x*y
def Divide(x: float, y: float) -> float:
    return x/y
def Calc(x: int, y: int, operator: str) -> float:
    if operator == "+":
        return Addition(x, y)
    if operator == "-":
        return Subtract(x, y)
    if operator == "*":
        return Multiply(x, y)
    if operator == "/":
        return Divide(x, y)

while True:
    x = float(input("What's your first number?: "))
    print("+\n-\n*\n/")
    operator = input("Pick an operator: ")
    y = float(input("What's your next number?: "))
    result = Calc(x, y, operator)
    print(f"{x} {operator} {y} = {result}")
    while True:
        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if decision == 'n':
            os.system('cls')
            break
        elif decision == 'y':
            x = result
            print("+\n-\n*\n/")
            operator = input("Pick an operator: ")
            y = float(input("What's your next number?: "))
            result = Calc(x, y, operator)
            print(f"{x} {operator} {y} = {result}")