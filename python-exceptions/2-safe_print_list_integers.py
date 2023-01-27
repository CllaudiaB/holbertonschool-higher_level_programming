#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        elements = 0
        for i in range(x):
            if type(my_list[i]) == int:
                    print("{:d}".format(my_list[i]), end='')
                    elements += 1
        print()
    except TypeError:
        print()
    return elements
