#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tope = len(my_list)
    if idx >= tope:
        return (my_list)
    elif idx < 0:
        return (my_list)
    else:
        copia = my_list.copy()
        copia[idx] = element
        return (copia)
