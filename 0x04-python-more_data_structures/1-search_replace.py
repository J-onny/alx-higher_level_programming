#!/usr/bin/python3


def search_replace(my_list, search, replace):
"""    
    return ([elem if elem != search else replace for elem in my_list])
"""
def search_and_replace(my_list, search, replace):
  return [replace if x == search else x for x in my_list]
