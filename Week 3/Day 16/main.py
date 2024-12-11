from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeMachineOn = True
my_coffeeMaker = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()
all_coffees = menu.get_items()

while coffeMachineOn:
    prompt = input(f"What would you like? ({all_coffees}): ")
    if prompt == "off":
        coffeMachineOn = False
        break
    if prompt == "report":
        my_coffeeMaker.report()
    else:
        coffeeObj = menu.find_drink(prompt)
        if my_coffeeMaker.is_resource_sufficient(coffeeObj):
            if payment.make_payment(coffeeObj.cost):
                my_coffeeMaker.make_coffee(coffeeObj)
