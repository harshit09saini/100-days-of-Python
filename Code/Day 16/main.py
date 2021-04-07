from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()

is_on = True

while is_on:
    user_input = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_maker.report()
    else:
        drink = coffee_menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_maker.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)