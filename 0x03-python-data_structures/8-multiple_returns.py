#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence is None or length == 0:
        return (length, None)
    return (length, sentence[0])
