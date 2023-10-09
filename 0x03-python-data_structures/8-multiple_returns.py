#!/usr/bin/python3


def multiple_returns(sentence):
    sen_len = len(sentence)
    sen_empty = True if sen_len == 0 else False

    mul_ret = (sen_len,)

    if sen_empty:
        mul_ret += (None,)
    else:
        mul_ret += (sentence[0],)

    return mul_ret


if __name__ == "__main__":
    multiple_returns(sentence)
