#!/usr/bin/python3
"""
 Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing the Pascal’s \
    triangle of n
    """
    triangle =[]

    if n <= 0:
        return triangle

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            my_list = [1]
            for j in range(i - 1):
                my_list.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            my_list.append(1)
            triangle.append(my_list)
    return triangle
