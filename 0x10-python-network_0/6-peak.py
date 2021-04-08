!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """


def find_peak(int_list):
    """ xd """

    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return int_list[0]
    if len(int_list) == 2:
        return max(int_list)

    mid_point = int(len(int_list)/2)
    middle = int_list[mid_point]

    if middle > int_list[mid_point - 1] and middle > int_list[mid_point + 1]:
        return middle
    elif middle < int_list[mid_point - 1]:
        return find_peak(int_list[:mid_point])
    else:
        return find_peak(int_list[mid_point + 1:])
