# Importing random module
import random

# Creating function for picking card
def take_card():
    """This function will choose one card from the list. It uses choice method to choose randomly."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card

# Creating blackjack function
def blackjack(cards):
    """this blackjack card takes one parameter as input and provides the result on the basis of condition.
    If it will return 0 , it means you lose the game and if 1 it means you won the game. if both condition not
    satisfied it returns the sum of the list."""

    if sum(cards) == 21 and len(cards) == 2:
        return 1
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        if sum(cards) > 21:
            return 0
        else:
            return sum(cards)
    elif sum(cards) > 21 and 11 not in cards:
        return 0
    else:
        return sum(cards)