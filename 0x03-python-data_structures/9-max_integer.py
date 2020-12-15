#!/usr/bin/python3
def max_integer(my_list=[]):
        if my_list:
            tope = len(my_list)
            maximo = my_list[0]
            for i in range(1, tope):
                if my_list[i] > maximo:
                    maximo = my_list[i]
                else:
                    continue
            return (maximo)
        else:
            return
