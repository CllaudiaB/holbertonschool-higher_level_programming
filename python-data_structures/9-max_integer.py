#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_value = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
    return (max_value)
