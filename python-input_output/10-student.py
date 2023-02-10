#!/usr/bin/python3
"""
Student to JSON with filter
"""


class Student():
    """
    Class Student that defines a student by: based on 9-student.py
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                for i in attrs:
                    if i == key:
                        new_dict[key] = value
            return new_dict
        else:
            return self.__dict__
