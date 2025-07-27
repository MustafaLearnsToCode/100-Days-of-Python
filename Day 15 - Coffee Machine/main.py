MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${profit}")

def sufficient_resources(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry, there is not enough {i}")
            return False
    return True

def process_coins():
    print("Please insert your coins.")
    total = int(input("How many quarters?: ")) *0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that is not enough money. Money refunded")
        return False

def make_coffee(coffee, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {coffee} ☕️. Enjoy!")

def commands():
    print("Here are some useful commands:\n'report': cafe resources available\n'menu': the cafe menu\n'exit': exit the cafe\n'key': return to commands\n")
commands()

while True:
    action = input("What would you like to do?: ").lower()
    if action == 'exit':
        exit()
    elif action == 'key':
        commands()
    elif action == 'report':
        report()
    elif action == 'menu':
        print(f"An espresso - ${MENU['espresso']['cost']}")
        print(f"A latte - ${MENU['latte']['cost']}")
        print(f"A cappuccino - ${MENU['cappuccino']['cost']}")
    else:
        drink = MENU[action]
        if sufficient_resources(drink["ingredients"]):
            print(f"It costs ${drink['cost']}")
            payment = process_coins()
            if transaction(payment, drink['cost']):
                make_coffee(action, drink['ingredients'])
                



