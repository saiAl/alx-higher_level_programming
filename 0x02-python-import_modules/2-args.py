#!/usr/bin/python3

import sys

if len(sys.argv) <= 1:
    print("0 arguments.")
else:
    length = len(sys.argv) - 1
    if length > 1:
        print("{:d} arguments:".format(length))
    else:
        print("{:d} argument:".format(length))

    for idx, value in enumerate(sys.argv):
        if idx >= 1:
            print("{:d}: {:s}".format(idx, value))
