#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    res = 0
    for idx, value in enumerate(sys.argv):
        if idx >= 1:
            res += int(value)
    print("{:d}".format(res))
