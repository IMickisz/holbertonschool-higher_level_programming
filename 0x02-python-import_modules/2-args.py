#!/usr/bin/python3
import sys

if __name__ == '__main__':
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print(" 1 argument:")
        print("1: {:s}".format(argv[1]))
    if len(argv) > 2:
        print("{:d} arguments:".format(len(argv) - 1))
        for argument in range(1, len(argv)):
            print("{:d}: {:s}".format(argument, argv[argument]))
