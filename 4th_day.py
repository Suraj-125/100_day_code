# Rock Scissor Paper Game

# First import the random module
import random

# Initializing the list items
user = ["rock", "scissor", "paper"]

# User input to choose between 0,1 and 2
choose = int(input("Choose a number between 0, 1 and 2 : "))

# If user choose above than 2, it will print invalid number
if choose >= 3 or choose < 0:
    print("This is a invalid number. Choose between 0, 1 and 2 ")

# If itt is between 0 and 2 , then else block will continue
else:

    # Printing the list item using input number
    print(f"You choose {user[choose].upper()}")

    # Using random module to provide random number between 0 and 2
    comp_choose = random.randint(0, 2)

    # Fetching the list item using random number
    computer_choose = user[comp_choose]
    print(f"Computer choose {computer_choose.upper()}")

    # If input and random number (both value) are equal, then it is draw
    if choose == comp_choose:
        print(" It,s Draw ")

    # If user choose 0, computer 1 then user wins or computer wins
    elif choose == 0:
        if comp_choose == 1:
            print(" You wins ")

        else:
            print(" Computer wins ")

    # If user choose 1, computer 0 then computer wins or user wins
    elif choose == 1:
        if comp_choose == 0:
            print("Computer wins")

        else:
            print("You wins")

    # If user choose 2, computer 0 then user wins or computer wins
    elif choose == 2:
        if comp_choose == 0:
            print("You wins")

        else:
            print("Computer wins")


