#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    conjunto1 = set(set_1)
    conjunto2 = set(set_2)
    diferencias = conjunto1 ^ conjunto2
    return (diferencias)
