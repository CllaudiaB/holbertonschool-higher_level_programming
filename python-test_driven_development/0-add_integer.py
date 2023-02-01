#!/usr/bin/python3
"""
Integers addition
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
