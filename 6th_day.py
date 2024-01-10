# ATM Project

# Account Details
pin = "1234"
account = "123456789012"
balance = 9000
mobile = "1234567890"


# Function to withdraw balance
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw : "))
    if balance >= amount:
        balance -= amount
        print(f"{amount} is withdrawl successfully. ")
        print(f"{balance} is left in the account. ")
        print("----------------Thanks for choosing SBI ATM--------------------")

    else:
        print(f"Insufficient balance : {balance}")
        print("----------------Thanks for choosing SBI ATM--------------------")


# Function to balance enquiry
def enquiry():
    global balance

    print(f"Hey, You have total {balance} rupees in your account. ")
    print("----------------Thanks for choosing SBI ATM--------------------")


# Function to provide report of account
def report():
    global balance
    global account
    global mobile

    account_number = account[8:]
    mobile_number = mobile[8:]

    print("-----------------Account Details----------------------")
    print(f"""
    Account Number : XXXXXXXX{account_number}
    Mobile Number  : XXXXXXXX{mobile_number}
    Total Amount   : {balance}
    """)
    print("----------------Thanks for choosing SBI ATM--------------------")

# Function to change pin number
def change_pin():
    global pin
    global mobile

    mobile_number = input("Enter 10 digit mobile number : ")
    while len(mobile_number) != 10:
        print("Mobile number must be 10 digit.")
        mobile_number = input("Enter 10 digit mobile number : ")

    if mobile == mobile_number:
        old_pin = input("Enter your previous 4-digit pin :")
        while len(old_pin) != 4:
            print("PIN number must be 4 digit.")
            old_pin = input("Enter your previous 4-digit pin  : ")

        if pin == old_pin:
            new_pin = input("Enter new 4-digit pin :")
            while len(old_pin) != 4:
                print("PIN number must be 4 digit.")
                new_pin = input("Enter new 4-digit pin  : ")

            print("You pin is successfully created.")
            print("----------------Thanks for choosing SBI ATM--------------------")

        else:
            print("You previous pin doesn't matched.")
            print("----------------Thanks for choosing SBI ATM--------------------")

    else:
        print("Mobile number not matched.")
        print("----------------Thanks for choosing SBI ATM--------------------")


# Function To deposit balance
def deposit():
    global balance

    amount = int(input("Enter amount to be added : "))

    if amount % 10 == 0:

        two_thousand = int(input("Enter 2000 note  : "))*2000
        five_hundred = int(input("Enter 500 note  : "))*500
        two_hundred = int(input("Enter 200 note  : "))*200
        one_hundred = int(input("Enter 100 note  : "))*100
        fifty = int(input("Enter 50 note  : "))*50
        twenty = int(input("Enter 20 note  : "))*20
        ten = int(input("Enter 10 note  : "))*10

        total = two_thousand + five_hundred + one_hundred + two_hundred + fifty + twenty + ten

        if amount == total:

            print(f"{amount} is successfully added.")
            balance += total
            print("Now, your total balance is", balance)
            print("----------------Thanks for choosing SBI ATM--------------------")

        else:

            print("Notes not matched.")
            print("----------------Thanks for choosing SBI ATM--------------------")

    else:
        print("We can't accept amount notes which is less than 10. ")
        print("----------------Thanks for choosing SBI ATM--------------------")


# ATM Starting

print("------------------Welcome to SBI ATM---------------------")

account_no = input("Enter your 12-digit account number :")
while len(account_no) != 12:
    print("Account number must be 12 digit.")
    account_no = input("Enter your 12-digit account number :")

pin_no = input("Enter your 4-digit pin :")
while len(pin_no) != 4:
    print("PIN number must be 4 digit.")
    pin_no = input("Enter your  4-digit pin  : ")

if account_no == account and pin == pin_no:
    print("Welcome User to your Account")

    preference = input("""Choose your preference :
                            1. Balance Enquiry
                            2. Balance Withdrawl
                            3. Deposit Balance
                            4. Change Pin
                            5. Balance Report
            Choose by typing 1,2,3,4,5............""")

    if preference == "1":
        # Enquiry function called
        enquiry()

    elif preference == "2":

        # Withdrawl Function called
        withdraw()

    elif preference == "3":

        # Deposit Function called
        deposit()

    elif preference == "4":

        # Change_pin function called
        change_pin()

    elif preference == "5":

        # Report function called
        report()

    else:
        print("Invalid preference. ")
        print("----------------Thanks for choosing SBI ATM--------------------")


else:
    print("Invalid Credidentals.")
    print("----------------Thanks for choosing SBI ATM--------------------")