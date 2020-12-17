#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    div = 0
    if my_list:
        for tup in my_list:
            a, b = tup
            res += a * b
            div += b
        return res / div
    return 0
