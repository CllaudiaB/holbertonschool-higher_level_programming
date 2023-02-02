#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these \
    characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    j = 0
    for i in text:
        if j == 0:
            if i == " ":
                continue
            else:
                j = 1
        if j == 1:
            if i == '.' or i == '?' or i == ':':
                print(i + '\n')
                j = 0
            else:
                print(i, end='')
