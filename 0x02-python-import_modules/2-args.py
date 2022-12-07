#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n <= 1:
        print("{:d} arguments.".format(n-1))

    elif n == 2:
        print("{:d} argument:".format(n-1))
        for i in range(1, n):
            print("{:d}: {}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(n-1))
        for i in range(1, n):
            print("{:d}: {}".format(i, argv[i]))

