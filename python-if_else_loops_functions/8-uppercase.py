#!/usr/bin/python3
def uppercase(str):

        for i in range(0, len(str)):
            n = ord(str[i])
            if n >= 97 and n <= 122:
                n = n - 32
            l = chr(n)
            print("{:s}".format(l), end='')
        print("")
