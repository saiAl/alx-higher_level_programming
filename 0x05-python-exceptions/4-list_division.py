#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new = list()
    res = 0
    idx = 0

    while idx < list_length:
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except (TypeError, ZeroDivisionError, IndexError):
            res = 0

            if not isinstance(my_list_2[idx], (int, float)):
                print("wrong type")
            elif my_list_2[idx] == 0 and isinstance(my_list_1[idx],
                    (int, float)) and isinstance(my_list_2[idx], (int, float)):
                print("division by 0")
            else:
                print("out of range")
        finally:
            new.append(res)
            idx += 1

    return new
