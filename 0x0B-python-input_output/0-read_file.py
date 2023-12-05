#!/usr/bin/python

def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
    print(data)
