#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(a, b):
            c = add(c, i)
        return c 
    sub(a, b)
    return None

dis.dis(magic_calculation)
