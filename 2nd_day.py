
# Tip Calculator - Day 2 ---

print("Welcome to the Tip Calculator ! ")
bill = float(input("What was the total bill ? "))
tip = int(input("How much tip would you like to give ? 10, 12 or 15 : "))
people = int(input("How many people you want to split the bill ?  "))

bill_with_tip = (((tip/100)*bill) + bill)/people

print(f"Each people have to pay {round(bill_with_tip,2)}")