#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    tope = len(my_list)
    for i in range(0, tope):
        if new_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
