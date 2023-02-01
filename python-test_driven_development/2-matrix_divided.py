#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """ div matrix """
    new = []
    result = []
    if div == float('inf'):
        raise TypeError('div must be a number')
    if matrix is None or div is None:
        raise TypeError("matrix_divided() missing 2 required \
positional arguments: 'matrix' and 'div'")
    for row in matrix:
        for j in row:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
 integers/floats")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        new.append(list(map(lambda x: x / div, matrix[i])))
    result = [[round(x, 2) for x in row] for row in new]
    return result
