#!/usr/bin/python
"""
@Author: John
"""
import json

def to_json_string(my_obj):
	"""
	Returs a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
	"""
	j_string = json.dumps(my_obj)
	return(j_string)
