import math

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


def print_report(resource, current_profit):
    print(f'Water: {resource["water"]}ml')
    print(f'Milk: {resource["milk"]}ml')
    print(f'Coffee: {resource["coffee"]}g')
    print(f'Money: ${current_profit}')


def is_resource_enough(d_water, d_milk, d_coffee, resource):
    if resource["water"] < d_water:
        print("Sorry there is not enough water.")
        return False
    elif resource["milk"] < d_milk:
        print("Sorry there is not enough milk.")
        return False
    elif resource["coffee"] < d_coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def check_resource(resource, user_choice):
    if user_choice not in MENU:
        print("Command not recognized. Try again")
    else:
        recipe = MENU[user_choice]["ingredients"]
        return is_resource_enough(recipe["water"], recipe["milk"], recipe["coffee"], resource)


def process_coins():
    print("Please insert coins: ")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    # Comment this out
    print(f"{quarters} + {dimes} + {nickles} + {pennies}")
    return math.fsum([quarters + dimes + nickles + pennies])


def transaction_successful(chosen_drink):
    inserted_coins = round(process_coins(), 2)
    chosen_coffee = MENU[chosen_drink]
    print(f'Inserted Coins: {inserted_coins}  / Coffee Cost: {chosen_coffee["cost"]}')

    if inserted_coins < chosen_coffee["cost"]:
        return False
    else:
        return True


def machine_start():
    global profit
    machine_running = True

    while machine_running:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == 'off':
            # Off Feature
            print("Turning off the machine! Have a nice day!")
            machine_running = False
        elif user_choice == 'report':
            # Report Feature
            print_report(resources, profit)
        else:
            # Coffe Feature
            if check_resource(resources, user_choice):
                if transaction_successful(user_choice):
                    # TODO 7: Make coffee
                    print("Continue process")
                else:
                    print("Sorry that's not enough money. Money refunded")
                    machine_running = False

# TODO: Possible Bug, no milk ingredients
machine_start()
