"""
This is Blackjack game of Day 11. Basically, it is a card game where user or computer won the game by scoring higher
but not more than 21. If they score more than 21 then they lose.
Rules of Blackjack Game :
1. Firstly two cards where choosen on random basis for both user and computer.
2. If user/computer got 21 by summing both values then they win but this win only happen when there is two card.
3. If getting less than 21 , then choose another card from deck.
4. Now sumup, if more than 21 then check whether it has 11, if there is 11 then convert it to 1 and sum it again. If
after converting 1 it results more than 21 , then you lose.
5. Last win is declared on the basis of priority.

That's it
"""

# Importing all the functions from module
from blackjack_module import *

# Creating function
def play_game():

    # Creating empty list to store user and computer cards
    user_card = []
    computer_card = []

    # Appending in the list
    for i in range(2):
        user_card.append(take_card())
        computer_card.append(take_card())

    # Flag for while
    show = True
    while show:

        # Calling blackjack function
        user = blackjack(user_card)
        computer = blackjack(computer_card)
        print(f"User cards are : {user_card} and their total sum is : {sum(user_card)}")
        print(f"Computer cards is : {computer_card} and it sum is : {sum(computer_card)}")

        # Resulting result on the basis of condition
        if user == 1 and computer == 1:
            print ("You both draw the game by blackjack 🤽.")
            break

        elif user == 1:
            print("You won the game by blackjack 🖤")
            break

        elif computer == 1:
            print("Computer won the game by blackjack.🖤")
            break

        elif user == 0:
            print("You lose because you cross over 21 ❌")
            break

        elif computer == 0:
            print("You won because computer cross over 21 ❌")
            break

        else:
            # Asking user to draw another card
            user_deck = input("Would you want to take another card yes or no : ")

            if user_deck == "yes":
                # Appending it to empty list
                user_card.append(take_card())
                show = True

            elif user_deck == "no":
                if computer < 17 :
                    # Appending it to computers empty list
                    computer_card.append(take_card())
                    show = True

                # Result providing basis on condition
                else:
                    if user == computer:
                        print (f"You both draw the game by scoring {user}  🟰 {computer}.")
                        break

                    elif computer > user:
                        print(f"Computer won the game by scoring {computer} 🪘.")
                        break

                    else:
                        print(f"You won the game by scoring {user} 🏆")
                        break



# Calling the play_game function
play_game()

# Initializing while loop as true
while True:
    start = input("Would you want to play again yes or no : ")
    if start == "yes":
        print("=============================BLACK - JACK  GAME ==============================")
        play_game()
    elif start == "no":
        print("Thanks for playing Black jack game.")
        break

"""That's the end of the game. Use this game it will clear all you basics of python"""
