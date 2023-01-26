#!/usr/bin/python3
def roman_to_int(roman_string):

    dictionary_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,\
                  'M': 1000}
    value = 0
    if type(roman_string) != str or not dictionary_r:
        return 0

    for i, element in enumerate(roman_string):
        if i != (len(roman_string) - 1) and dictionary_r[element]\
           < dictionary_r[roman_string[i + 1]]:
            value -= dictionary_r[element]
        else:
            value += dictionary_r[element]
    return value
