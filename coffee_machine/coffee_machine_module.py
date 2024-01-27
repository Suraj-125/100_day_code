# Dictionaries of items and total ingredients
items = {
    "coffee": {
        "ingredients": {
            "water": 200,
            "sugar": 100,
            "coffee": 50,
            "milk": 25
        },
        "cost": 25
    },
    "tea": {
        "ingredients": {
            "water": 150,
            "sugar": 120,
            "tea": 35,
            "milk": 40
        },
        "cost": 15
    },
    "milky": {
        "ingredients": {
            "water": 80,
            "sugar": 50,
            "milk": 130
        },
        "cost": 30
    }
}


total_ingredients = {
    "water": 2000,
    "sugar": 1000,
    "milk": 1000,
    "tea": 500,
    "coffee": 600
}


def manage_ingredients (total_resources):
    """Check the total_resources is more than particular items"""
    for item in total_resources:
        if total_resources[item] > total_ingredients[item]:
            print(f"Sorry ! there is not enough {item}")
            return False
    return True


def make_item (choose, total_resources):
    """Subtract particular item ingredients from total ingredients."""
    for item in total_resources:
        total_ingredients[item] -= total_resources[item]
    print(f"Here is your {choose}. Enjoy ☕")



def your_choice(choose):
    """Returns the cost of choosen item"""
    if choose == "coffee":
        return items[choose]['cost']
    elif choose == "tea":
        return items[choose]['cost']
    elif choose == "milky":
        return items[choose]['cost']


