"""
This is a simple calculator created with the help of python. All operators are stored in dictionary and called when the
user wants it. It perform four operation addition, subtraction, multiplication and division. When user ends with calculation
it again start with 0. That's it about this project.
"""

# Four function created for performing calculation
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def divide(a, b):
    return a / b

# Function are stored in dictionary and is fetched with the help of keys which is expression
operators_func = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": divide
}

# Creating a calculator function
def calculator():

    # This is just a logo
    print('''
          CCCCCCC      CCCC       C          CCCCCCCCC  C      C   C            CCCC       CCCCCCCCCC   CCCCCCCC  CCCCCCCCCC
          C            C  C       C          C          C      C   C            C   C           C       C      C   C      C
          C           C    C      C          C          C      C   C           C     C          C       C      C   C      C
          C          C C C CC     C          C          C      C   C          C CCCCC C         C       C      C   CCCCCC
          C         C        C    C          C          C      C   C         C         C        C       C      C   C     C
          CCCCCCC  C          C   CCCCCCCC   CCCCCCCCC  CCCCCCCC   CCCCCCC  C           C       C       CCCCCCCC   C       C
    ''')

    # User to input first number
    num = float(input("Enter the first number : "))
    print("Choose the operators from below")

    # FEtching all the keys using looping
    for i in operators_func:
        print(i)

    # Using a flag to control while loop
    start = True

    while start:
        operators = input("Select the operators : ")

        # FEtch the value which is generally function as per user selection
        calculate = operators_func[operators]
        num2 = float(input("Enter the second number : "))

        # Calling the function and performing the result
        total = calculate(num, num2)
        print(f"After calculation total is  {total}")

        preference = input("Input 'yes' to continue and 'n' to discontinue : ")
        if preference == "yes":
            num = total

        else:
            start = False
            calculator()


calculator()

