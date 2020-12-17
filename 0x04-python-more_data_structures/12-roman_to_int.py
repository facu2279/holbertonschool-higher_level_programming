#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    int_num = 0
    i = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in range(0, len(roman_string)):
            if i < len(roman_string) - 1:
                if numbers[roman_string[i]] < numbers[roman_string[i + 1]]:
                    int_num -= numbers[roman_string[i]]
                    continue
            int_num += numbers[roman_string[i]]
    return int_num
