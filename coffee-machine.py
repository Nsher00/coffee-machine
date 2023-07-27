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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffe_machine():
    order = input('What would you like to order? 1. Espresso, 2. Latte, 3. Cappuccino')
    if order == '1':
        if resources["water"] > MENU['espresso']["ingredients"]["water"] and resources["coffee"] > MENU['espresso']["ingredients"]["coffee"]:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            print("your order was successful.")
            coffe_machine()

    elif order == '2':
        if resources["water"] > MENU['latte']["ingredients"]["water"] and resources["coffee"] > MENU['latte']["ingredients"]["coffee"] and resources["milk"] > MENU['latte']["ingredients"]["milk"]:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            print("your order was successful.")
            coffe_machine()

    elif order == '3':
        if resources["water"] > MENU['cappuccino']["ingredients"]["water"] and resources["coffee"] > MENU['cappuccino']["ingredients"]["coffee"] and resources["milk"] > MENU['cappuccino']["ingredients"]["milk"]:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            print("your order was successful.")
            coffe_machine()

    elif order == 'off':
        pass



if __name__ == '__main__':
    coffe_machine()