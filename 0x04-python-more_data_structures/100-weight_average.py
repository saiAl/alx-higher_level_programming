#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total = div = mul = 0

    for item in my_list:
        mul = item[0] * item[1]
        total += mul
    for item in my_list:
        div += item[1]

    return float(total / div)
