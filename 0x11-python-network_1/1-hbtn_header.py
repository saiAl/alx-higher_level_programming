#!/usr/bin/python3
"""
displays the value of the X-Request-Id
    variable found in the header of the response
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    import sys
    with urlopen(str(sys.argv[1])) as res:
        print(res.getheader("X-Request-Id"))
