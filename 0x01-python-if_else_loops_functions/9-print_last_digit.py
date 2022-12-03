#!/usr/bin/python3
def print_last_digit(number):
    my_number = abs(number) % 10
    print("{:1}".format(my_number), end="")
    return my_number

