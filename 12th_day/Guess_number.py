"""
This is guess number game which has two level "easy" and "hard".
In "easy" you got 10 chances to guess the number.
In "hard" you got 5 chances to guess the number.
"""


# Importing module
from guess_module import *

# Providing input for level
option = input("Choose your difficulty level, 'hard' or 'easy' : ").lower()

# Generating random value 1 to 99
random_value = random.randint(1, 100)

# Calling hint function
hint = hint(random_value)
print(hint)

# Initializing start flag
start = 0
while start < level[option] :
    print("---------------------------------------------------------------------------------------")
    print(f"You have total {level[option] - start} chances left.")
    your_guess = int(input("Guess your number"))

    # Calling number_guess function
    result = number_guess(guess=your_guess, value=random_value)
    print(result)
    start += 1
print(f"You lose the game. Value is {random_value}.")






