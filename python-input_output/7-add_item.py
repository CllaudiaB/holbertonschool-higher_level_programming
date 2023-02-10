#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    args = sys.argv
    filename = "add_item.json"
    with open(filename, 'a+', encoding='utf-8') as f:
        try:
            my_list = load_from_json_file(filename)
        except:
            my_list = []
        my_list.extend(args[1:])
        save_to_json_file(my_list, filename)
