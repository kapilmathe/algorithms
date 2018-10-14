#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    st = []
    n = len(s)
    open_braces = dict(zip(list('({['), list(')}]')))
    for i in range(n):
        if s[i] in open_braces.keys():
            st.append(s[i])
        else:
            if len(st):
                val = st.pop()
                x = open_braces[val]
                # print(val, s[i])
                if x != s[i]:
                    return 'NO'
            else:
                return 'NO'
    if len(st):
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        # fptr.write(result + '\n')
        print(result)
    # fptr.close()
