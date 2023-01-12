#!/usr/bin/python
"""
@Author: John
"""
import json
def from_json_string(my_str):
	"""
		Convert a json string to a python object

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A Python object from json
	"""
	d_string= json.loads(my_str)
	return(d_string)
