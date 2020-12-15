#!/usr/bin/python3
def element_at(my_list, idx):
    tope = len(my_list)
    if idx > tope:
        return
    elif idx < 0:
        return
    else:
        return (my_list[idx])
