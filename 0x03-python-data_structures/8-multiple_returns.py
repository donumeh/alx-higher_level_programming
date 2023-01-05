#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_letter = None
    else:
        first_letter = sentence[0]

    tp = len(sentence), first_letter
    return tp
