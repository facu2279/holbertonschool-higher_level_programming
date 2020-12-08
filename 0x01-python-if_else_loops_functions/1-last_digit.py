#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negativo = 0
if number < 0:
    negativo = 1
    number = number * -1
lastdigit = number % 10

if negativo == 1:
    number = number * -1
    lastdigit = lastdigit * -1
print("Last digit of", '{:d}'.format(number), end="")
print("is", '{:d}'.format(lastdigit), end="")
if lastdigit > 5:
    print(" and is greater than 5")
elif lastdigit < 6:
    print(" and is less than 6 and", end="")
    if lastdigit != 0:
        print(" not 0")
elif lastdigit == 5:
    print(" is 5 and is less than 6 and not 0", end="")
if lastdigit == 0:
    print("and is 0")
