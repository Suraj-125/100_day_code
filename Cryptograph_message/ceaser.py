from cipher import confidential

show = True
while show:
    option = input("Enter encode or decode: ")
    name = input("Enter your name : ")
    shift = int(input("shift number : "))

    confidential(name, shift, option)

    opinion = input("Would you want to continue : Type y for yes and n for no : ").lower()

    if opinion == "y":
        show = True
    elif opinion == "n":
        break

