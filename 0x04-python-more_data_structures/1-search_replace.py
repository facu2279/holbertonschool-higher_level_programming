#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    tope = len(my_list)

    for i in range(0, tope):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
