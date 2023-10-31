#!/usr/bin/python3

ch = 122
pos = 0

while (ch > 96):
    pos += 1

    if (pos % 2 == 0):
        letter = ch - 32
        pos = 0
    else:
        letter = ch

    print("{:s}".format(chr(letter)), end='')
    ch -= 1
