#!/usr/bin/python3
def islower(c):
    for i in (range(ord('a') and ord('Z'))):
        if ord(c) > 96 and ord(c) < 123:
            return True
        else:
            return False

