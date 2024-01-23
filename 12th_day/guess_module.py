# Importing sys and random module
import sys
import random

# Dictionary
level = {
    "hard": 5,
    "easy": 10
}

# Creating number_guess function
def number_guess (guess , value):
    if guess == value:
        print("Hurrah ! You got it.")
        # using sys.exit to terminate the block
        sys.exit()
    elif guess != value:
        if value > guess:
            difference = value - guess
            if difference > 20:
                return "You are too low."
            elif difference > 10:
                return "You are low but near about it."
            elif difference > 5:
                return "You are little bit low."
            else:
                return "Ahh ! you are too close."

        elif value < guess:
            difference = guess - value
            if difference > 20:
                return "You are too high."
            elif difference > 10:
                return "You are high but near about it."
            elif difference > 5:
                return "You are little bit high."
            else:
                return "Ahh ! you are too close."


# Creating hint function
def hint(value):
    if value <= 50:
        return "It's range between 1 to 50."
    elif value > 50:
        return "It's range between 51 to 99."

