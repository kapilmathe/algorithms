#!/bin/python

import math
import os
import random
import re
import sys


def is_balanced(s):
    stk = []
    if len(s)%2:
        return 'NO'
    else:
        opening_br = {'[': 1, '{': 1, '(': 1}
        closing_br = {']': 1, '}': 1, ')': 1}
        for x in s:
            if x in opening_br:
                stk.append(x)
            elif x in closing_br:
                if len(stk):
                    last_in = stk.pop()
                    # print("last_in={0}".format(last_in))
                    if ord(last_in) - ord(x) < 3:
                        continue
                    else:
                        return 'NO'
                else:
                    return 'NO'
            else:
                return 'NO'
        if len(stk):
            return 'NO'
        else:
            return 'YES'


if __name__ == '__main__':
    t = int(raw_input())
    result = []
    for t_itr in xrange(t):
        expression = raw_input()
        print(is_balanced(expression))

