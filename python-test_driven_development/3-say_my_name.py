#!/usr/bin/python3
"""
Say my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name is None and last_name is None:
        raise TypeError("say_my_name() missing 2 required positional arguments:\
                'first_name' and 'last_name'")
    print("My name is {} {}".format(first_name, last_name))
