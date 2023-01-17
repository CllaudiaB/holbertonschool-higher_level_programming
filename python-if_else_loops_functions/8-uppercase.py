#!/usr/bin/python3
def uppercase(str):
    if len(str) != 0:
        for i in range(0, len(str)):
            n = ord(str[i])
            if n >= 97 and n <= 122:
                n = n - 32
            l = chr(n)
            if i == len(str) - 1:
                print("{:s}".format(l))
            else:
                print("{:s}".format(l), end='')
        else:
            return str
