#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if len(str) == 0:
            return
        n = ord(str[i])
        if n >= 97 and n <= 122:
            n = n - 32
        l = chr(n)
        if i == len(str) - 1:
            print("{:s}".format(l))
        else:
            print("{:s}".format(l), end='')
