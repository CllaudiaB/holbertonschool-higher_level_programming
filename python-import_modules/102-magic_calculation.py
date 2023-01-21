#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
    else:
        for i in range(4, 6):
            c = add(c, i)
            return c
        sub(a, b)
