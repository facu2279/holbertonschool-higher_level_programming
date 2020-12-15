#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list:
        tope = len(my_list)
        if idx >= tope:
            return
        elif idx < 0:
            return
        else:
            return (my_list[idx])
