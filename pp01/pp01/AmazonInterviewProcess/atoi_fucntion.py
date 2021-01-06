import math
import os
import random
import re
import sys


def atoi_function(inp_str):
    if isinstance(inp_str, int):
        return inp_str
    else:
        if inp_str is None:
            return inp_str
        if isinstance(inp_str, str):
            n = len(inp_str)
            i=n-1
            out = 0
            digit = 1
            while i >=0:
                out += digit*int(inp_str[i])
                digit *=10
                i -= 1
            return out
        else:
            return inp_str


if __name__ == '__main__':
    inp = input().strip()
    print(type(inp))
    print("input value = {0}".format(inp))
    out = atoi_function(inp)
    print("output value = {0}".format(out))
    print(type(out))
