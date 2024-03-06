from menu import MENU
from menu import resources

profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    total = int(input("Please insert coins: "))
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("Menu and Prices:")
        for item, details in MENU.items():
            print(f"{item.capitalize()}: ${details['cost']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink.get("ingredients", {})):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink.get("ingredients", {}))
        else:
            print("Invalid choice. Please select again.")