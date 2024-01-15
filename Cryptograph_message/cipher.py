alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z", ",", ".", "=", "@", "#", "$", "%", "^", "*", "&", "<", ">",
            "/", ";", ":"]



def confidential(n, s, o):
    message = ""
    for i in n:
        number = alphabet.index(i)
        if o == "encode":
            if s % 10 == 0:
                total = number + 3
                message += alphabet[total]
            else:
                rem = s % 10
                total = number + rem
                message += alphabet[total]

        elif o == "decode":
            if s % 10 == 0:
                total = number - 3
                message += alphabet[total]
            else:
                rem = s % 10
                total = number - rem
                message += alphabet[total]

    print(message)






