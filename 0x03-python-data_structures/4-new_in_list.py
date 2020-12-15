#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        my_list2 = my_list.copy()
        my_list2[idx] = element
        return my_list2
