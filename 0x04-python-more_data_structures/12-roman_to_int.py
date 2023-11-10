#!/usr/bin/python3


def roman_to_int(roman_string):
    """
        roman_to_int - function converts a roman string to an integer

        Args:
            roman_string (str): a string
        Returns:
            return the integer
    """

    if type(roman_string) != str or roman_string is None:
        return 0

    integers = 0

    roman_list = word_list(roman_string)
    numbers = list()
    for roman_w in roman_list:
        numbers += convert_int(roman_w)

    for n in numbers:
        integers += n

    return int(integers)


def convert_int(word=""):
    """
        convert_int - function to convert a roman string to integers

        Args:
            word (str): roman word
        Return:
            converted integers
    """
    uni = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
    ten = {"X": 1, "XX": 2, "XXX": 3, "XL": 4, "L": 5, "LX": 6, "LXX": 7, "LXXX": 8, "XC": 9}
    hun = {"C": 1, "CC": 2, "CCC": 3, "CD": 4, "D": 5, "DC": 6, "DCC": 7, "DCCC": 8, "CM": 9}
    tho = {"M": 1, "MM": 2, "MMM": 3}

    dicts = [uni, ten, hun, tho]
    idx = 0
    mul = 1
    res = 0
    ints = list()

    while idx < 4:
        for key, value in dicts[idx].items():
            if word == key:
                match idx:
                    case 1:
                        mul = 10
                    case 2:
                        mul = 100
                    case 3:
                        mul = 1000
                res = int(dicts[idx][key]) * mul
                ints.append(res)
        idx += 1
    return ints


def word_list(s=""):
    """
        word_list - function that return a list of roman words

        Args:
            s (str): roman string
        Return:
            a list of roman words

    """

    word = ""
    length = len(s)
    start = int(length / 2)
    values = list()

    if length <= 4:
        values.append(s)
    else:
        match length:
            case 5:
                for i in range(0, length - start):
                    word += s[i]
                values.append(word)
                word = ""
                for i in range(1 + start, length):
                    word += s[i]
                values.append(word)
            case 7:
                for i in range(0, length - start):
                    word += s[i]
                values.append(word)
                word = ""
                for i in range(1 + start, length):
                    word += s[i]
                values.append(word)

            case _:
                for i in range(0, length - start):
                    word += s[i]
                values.append(word)
                word = ""
                for i in range(start, length):
                    word += s[i]
                values.append(word)
    return values
