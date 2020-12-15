#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        copia = my_list.copy()
        tope = len(my_list)
        if idx > tope:
            return (copia)
        elif idx < 0:
            return (copia)
        else:
            copia[idx] = element
            return (copia)
    else:
        return
