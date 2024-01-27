# Importing all functions and dictionaries from index file
from coffee_machine_module import *
# Flag to store the total sell amount
profit = 0


def check_price(price_amount, pay_amount):
    """Returns true if pay_amount is more otherwise false"""
    global profit
    if price_amount <= pay_amount:
        amount_to_return = pay_amount - price_amount
        print(f"You paid {pay_amount} rupees and here's your extra {amount_to_return} rupees.")
        profit += price_amount
        return True
    else:
        amount = price_amount - pay_amount
        print(f"Sorry ! you paid {amount} rupees less. We can't process further.")
        return False


# flag
is_machine = True
# loop to iterate again and again
while is_machine:
    print("-------------------------------WELCOME TO COFFEE MACHINE-----------------------------------")
    choice = input("What can i serve to you . Coffee, Tea, Milky : ").lower()
    if choice == "off":
        is_machine = False
    elif choice == "report":
        # Provide report of total ingredients.
        resource = total_ingredients
        print("------------REPORT------------------")
        print(f"Amount of water left {resource['water']}")
        print(f"Amount of sugar left {resource['sugar']}")
        print(f"Amount of milk left {resource['milk']}")
        print(f"Amount of coffee left {resource['coffee']}")
        print(f"Amount of tea left {resource['tea']}")
        print(f"Total Profit {profit} rupee.")
        print("-------------------------------")
    else:
        resources = items[choice]['ingredients']
        # Calling your_choice function
        price = your_choice(choice)
        # Calling manage_ingredients function
        if manage_ingredients(resources):
            print(f"Cost of a {choice.upper()} is {price} rupees.")
            pay = int(input("We are ready to accept the amount. Pay ! Please : "))
            # Calling check_price function
            if check_price(price, pay):
                # Calling make_item function
                make_item(choice, resources)






















