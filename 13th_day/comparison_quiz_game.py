# Importing details
from celebrity_details import detail

# Importing random
import random

# Flag
A = ""
score = 0
count = 0

# Function to choose randomly a dictionaries
def your_choice(choice):
    a = random.choice(detail)
    name = a["name"]
    role = a["role"]
    rating = a["rating"]
    global A
    A = a["follower"]
    return f"{name} works as a {role} and he acheived {rating} rating."

while count < 10:

    print("Predict who has most number of follower.")
    print(f"""
    ------------------------
    Your Score = {score}
    ------------------------
    """)

    print(f"""
    ---------------------------------QUESTION {count + 1}----------------------------------
""")

    # Calling function
    first = your_choice(detail)
    print("A.",first)
    a_follower = A

    print("                        VS ")

    # Calling function
    print("B.", your_choice(detail))
    b_follower = A

    # Input to enter for user
    ask = input("Who has most number of follower : A or B : ").lower()

    # Conditional Statement for priority
    if ask == "a":
        if a_follower > b_follower:
            print(f"Great you guess right. He has {a_follower} follower.")
            score += 1
            count += 1

        else:
            print(f"No, it's not a right guess. Guess another one.")
            count += 1

    elif ask == "b":
        if a_follower < b_follower:
            print(f"Great you guess right. He has {b_follower} follower.")
            score += 1
            count += 1

        else:
            print(f"No, it's not a right guess. Guess another one.")
            count += 1


# Conditional statement for result
print("======================= RESULT =================================")
print(f"Out of 10 you answered {score} correct and {10 - score} incorrect")
if score > 8:
    print("You got 1st division")
elif score > 6:
    print("You got 2nd division")
elif score > 4:
    print("You got 3rd division")
else:
    print("You Fail the game.")
print("=================================================================")