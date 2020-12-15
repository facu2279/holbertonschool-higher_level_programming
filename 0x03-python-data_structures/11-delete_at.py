#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
        tope = len(my_list)
        if idx < tope and idx > 0:
            del my_list[idx]
        
        return (my_list)
