#!/usr/bin/python3
def print_last_digit(number):
    negativo = 0
    if number < 0:
        number = number * -1
        negativo = 1
    lastdigit = number % 10

    if negativo == 1:
        number = number * -1

    print('{:d}'.format(lastdigit), end="")
    return(lastdigit)
