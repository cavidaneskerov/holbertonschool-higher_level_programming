#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 0:
        print("{} arguments.".format(len()argv-1))
    elif len(argv) == 1:
        print("1 argument:")
        print("{}: {}".format(len()argv-1, argv[1]))
    else:
        print("{} arguments:".format(len(argv)-1))
        for i in range(1, len(argv)-1):
            print("{}: {}".format(i, argv[i]), end="\n")
        print("{}: {}".format(len(argv)-1, argv[-1]))
