#!/usr/bin/python3
def common_elements(set_1, set_2):
    conjunto1 = set(set_1)
    conjunto2 = set(set_2)
    elementos_comunes = conjunto1 & conjunto2
    return (elementos_comunes)
