#!/usr/bin/python3
def roman_to_int(roman_string):

    d_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    if type(roman_string) != str or not d_roman:
        return 0

    for i, element in enumerate(roman_string):
        if i != (len(roman_string) - 1) and d_roman[element]\
           < d_roman[roman_string[i + 1]]:
            value -= d_roman[element]
        else:
            value += d_roman[element]
    return value
