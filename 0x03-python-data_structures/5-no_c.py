#!/usr/bin/python3
def no_c(my_string):
    my_list = ""
    tope = len(my_string)
    for i in range(0, tope):
        if my_string[i] == "C" or my_string[i] == "c":
            continue
        my_list = my_list + my_string[i]
    return(my_list)
