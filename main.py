import random



numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
           "u", "v", "w", "x", "y", "z",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]


symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
           "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|",
           ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?",
           "~", "`"]



def randomINT():
    print(random.choice(numbers))

import random


def randomFLOAT(x):
    before_decimal = random.choice(numbers)
    after_decimal = ''.join(random.choice(numbers) for _ in range(x)) 
    random_float = float(before_decimal + "." + after_decimal)
    print(random_float)


randomFLOAT(6)





