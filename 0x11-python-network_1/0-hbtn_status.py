#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

"""
from urllib.request import urlopen
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()

print("- type: {}".format(type(body)))
print("- content: {}".format(body))
print("- utf8 content: {}".format(body.decode('utf-8')))
