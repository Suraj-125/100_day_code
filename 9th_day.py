# Creating an empty dictionary for auction member storage
auction = {}

# Defining a function to check who bid maximum
def maximum_bid(bidding):

    # Initializing highest to store highest value
    highest = 0

    # Initializing winner to store highest bid name
    winner = ""

    # Iterating the dictionary in sequential manner using for loop
    for bide in bidding:

        # Checking the bid value is greater or smaller than the highest value stored above
        if bidding[bide] > highest:

            # Assign the bid value if it is more
            highest = bidding[bide]

            # Also assign the winner name
            winner = bide

    # Show the winner and highest bid
    print(f"The highest bid is {highest}$ and winner is {winner}")

# Initializing false to process variable
process = False

# When process is true condition satisfies
while not process:

    # Input name for bid
    name = input("Enter your name : ")

    # Input bid amount
    bid = int(input("Enter your bid amount : $"))

    # Storing the input name bid in auction dictionary
    auction[name] = bid

    # Input to iterate or terminate the bidding process
    decision = input("Anyone wanted to bid 'yes' or 'no' : ")

    # If input is yes then iterate else terminate the bidding process
    if decision == "no":

        # Calling the maximum_bid function
        maximum_bid(bidding=auction)

        # Input is no , so assigning True to the process
        process = True

# For justification print the auction dictionary
print(auction)
