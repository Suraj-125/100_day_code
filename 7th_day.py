"""
Hangman Game is guessing word game. Step of this game ---
1. If you guess, right then your man safe
2. If wrong, then it is hanged.
3. Hangman will died, when its head, hand and legs are hanged. And this will possible when you will provide maximum wrong word.
4. If you will guess correct word, you will won and the hangman become safe.
That's a simple game. Make it and enjoy the game.
"""



# Hangman is stored in a list with the help of docstring
hangman = ["""
'   _______
    |     |
    |
    |
    |
    |
'
""", """         
'   _______
    |     |
    |     O
    |
    |
    |
'
""", """ 
'   _______
    |     |
    |     O
    |     |
    |
    |
'
""", """ 
'   _______
    |     |
    |     O
    |   / |
    |  
    |
'
""", """ 
'   _______
    |     |
    |     O
    |   / | ]
    |  
    |
'
""", """ 
'   _______
    |     |
    |     O
    |   / | ]
    |    /
    |
'
""", """ 
'   _______
    |     |
    |     O
    |   / | ]
    |    / [
    |
'
"""]


# These are words which we have to guess and it will be fetched randomly
word_list = ["pea", "beans", "carrot", "ladyfinger", "bittergaurd", "brinjal", "cabbage", "chilli", "cauliflower", "onion", "potato"]

# Now, importing random and taking the words in random order
import random
word = random.choice(word_list)
print(word)

# Print statement that it is related to vegetable
print("The word is related to vegetable.")

# Creating an empty list to store "_"
blank = []

# Using for loop to store exact number of blank that how much letter word contains.
for letter in word:
    blank.append("_")

# Initializing start to 0 and increase it slowely if user choose wrong word.
start = 0

# While loop to iterate 7 times
while start != 7:

    # First hangman will show its 0th index
    hang = hangman[start]
    print(hang)

    # Blank is printed to guess the length of word
    print(blank)

    # User input to choose the word and convert to lowercase and stripping it from right and left
    user = input("Enter the word : ").lower()
    user.strip()

    # If user word present in word then
    if user in word:

        # For loop checks the entire word where user word present
        for guess in range(len(word)):

            # If user word matches then it store the same index in blank where that word is present in word
            if user == word[guess]:
                blank[guess] = word[guess]

    # If not matched, we will increase start value by 1 which also increment the index of hangman
    else:
        start += 1

    # If "_" not present in blank then print you win and terminate the while loop
    if "_" not in blank:
        print("------------------------------------------------------")
        print("Congratulations ! You guess the word.")
        print("------------------------------------------------------")
        break
    # If start equal to 6 , print you lose, show last index of hangman and terminate the while loop
    if start == 6:
        hang = hangman[-1]
        print(hang)
        print("--------------------------------------------------------")
        print("Oops ! You lose the game.")
        print("--------------------------------------------------------")
        break


# That's the end of hangman game.




























