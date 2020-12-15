#!/usr/bin/python3
def no_c(my_string):
    tope = len(my_string)
    new_string = ""
    j = 0
    for i in range(0, tope):
        if my_string[i] != "c":
            new_string[j] = my_string[i]
        j = j + 1
    
    return (new_string)
