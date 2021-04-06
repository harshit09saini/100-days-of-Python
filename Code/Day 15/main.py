from data import MENU, resources

enough_resources = True


def format_resources():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\n" \
           f"Coffee: {resources['coffee']}\nMoney: ${resources['money']}"


def handle_money(price_bev, total_money):

    change = round((total_money - price_bev), 2)
    resources["money"] += price_bev
    return change


def check_resources(beverage):
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]
    required_water = MENU[beverage]["ingredients"]["water"]
    required_milk = MENU[beverage]["ingredients"]["milk"]
    required_coffee = MENU[beverage]["ingredients"]["coffee"]

    if required_water < current_water and required_coffee < current_coffee and required_milk < current_milk:
        return True
    else:
        return False


def update_resources(beverage):
    resources["water"] -= MENU[beverage]["ingredients"]["water"]
    resources["milk"] -= MENU[beverage]["ingredients"]["milk"]
    resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]


while enough_resources:
    user_beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_beverage == "off":
        exit()
    if user_beverage == "report":
        print(format_resources())
        continue

    print("\nPlease insert coins.\n")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    user_total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    user_total = round(user_total, 2)

    beverage_cost = MENU[user_beverage]["cost"]

    if user_total < beverage_cost:
        print("Sorry, not sufficient amount")
        continue

    to_return_change = handle_money(beverage_cost, user_total)

    if check_resources(user_beverage):
        print(f"Here is your {user_beverage} ☕. Enjoy.")
        print(f"Don't forget to pick up your change: ${to_return_change}")
        update_resources(user_beverage)
    else:
        print("Sorry, Not enough resources. The drink cannot be dispensed. You money is refunded.")
        enough_resources = False
