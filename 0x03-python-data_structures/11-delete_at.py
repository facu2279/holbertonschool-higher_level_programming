#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    tope = len(my_list)
    if idx < 0 or idx >= tope:
        return (my_list)

    del my_list[idx]
    return (my_list)
