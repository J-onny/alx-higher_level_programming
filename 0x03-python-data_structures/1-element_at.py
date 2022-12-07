#!/usr/bin/python3

def element_at(my_list, idx):
    if my_list:
        if idx < 0:
            return "None"
        if idx > len(my_list):
            return "None"

        for val in range(len(my_list)):
            if my_list.index(my_list[val]) == idx:
                return my_list[val]
