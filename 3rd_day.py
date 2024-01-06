print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Create a welcome for user
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

# Input your choices
choice1 = input("Which turn you want to take ? left or right - ").lower()

# If your choice is left , then it will execute forward and move to the next one
if choice1 == "left":
    print("="*90)
    print("Great, you took a right step . There is a river.")
    print("🤽"*21)

    # Input your choice2 , because you are in the game
    choice2 = input("Would you want to swim or wait ? - ").lower()

    # If you select wait, then it will execute and move to the next one
    if choice2 == "wait":
        print("=" * 90)
        print("Another Great step, You are a genious. Now there is a three door .")
        print("🚪"*21)

        # Input your choice3 , because you are in the game.
        choice3 = input("Which door you want to choose ? Red, Blue or Yellow - ").lower()

        # If your choice is red, then game over
        if choice3 == "red":
            print("=" * 90)
            print("No man ! this was a wrong door ? There are too many snake. Run from there now. ")
            print("🐍"*21)
            print("Snake caught and bite you . You died 😭😭")
            print("Game Over")

        # If your choice is blue , then game over.
        elif choice3 == "blue":
            print("=" * 90)
            print("Uff man ! this was a wrong door ? There is Annebella . Oh ! just get out from there. ")
            print("👻"*21)
            print("Annebella caught you and you become the diet of annebella 😭😭")
            print("Game Over")

        # If your choice is yellow, you win the game.
        elif choice3 == "yellow":
            print("=" * 90)
            print("Hurrah ! You done it. You are the real treasure hunter .")
            print("🪘"*21)
            print("You become the one of the richest man . Now you can also say that you are millioners.")
            print("You won the Game. Congrats 🪘🎊")

    # If your choice is swim, then game over
    else:
        print("=" * 90)
        print("Oh man ! what you have done ? If you don't know how to swim. They why you choose this decision. ")
        print("Damn it ! You sink in the river. You died 😭😭")
        print("Game Over")

# If your choice is right then game over
else:
    print("=" * 90)
    print("You entered in a cave and there was a lion. ")
    print("🦁"*21)
    print("Oh my God ! Lion ate you 😭😭")
    print("Game Over")
