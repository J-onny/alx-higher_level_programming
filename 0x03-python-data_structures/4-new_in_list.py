#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_own_list = my_list[:]
    list_lenght = len(my_list)
    if idx < 0 or idx >= list_lenght:
        return my_list
    else:
        my_own_list[idx] = element
        return my_own_list
