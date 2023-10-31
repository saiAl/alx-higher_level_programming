#!/usr/bin/python3

ch = 122
pos = 1

while (ch > 96):
    if (pos % 2 == 0):
        cap = ch - 32
        pos = 0
        print(chr(cap), end='')
    else:
        print(chr(ch), end='')
    
    pos += 1
    ch -= 1
