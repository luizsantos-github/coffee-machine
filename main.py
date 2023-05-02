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
    "coffee": 1,
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


def machine_start():
    machine_running = True

    while machine_running:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == 'off':
            print("Turning off the machine! Have a nice day!")
            machine_running = False
        elif user_choice == 'report':
            print_report(resources, profit)
        else:
            if check_resource(resources, user_choice):
                print("Nice Resource is enough!")

            # TODO 5. Process coins
            # TODO 6. Check if transaction is successful
            # TODO 7. Make Coffee


machine_start()
