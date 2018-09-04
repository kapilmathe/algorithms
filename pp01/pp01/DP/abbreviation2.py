def print_matrix(a, b):
    i = 0
    for l in a:
        print(b[i-1] if i > 0 else '-', " ".join([str(x) for x in l]))
        i += 1


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    m = len(a)
    n = len(b)
    if m == 0 and n ==0:
        return 'YES'
    if m == 0 and n > 0:
        return 'NO'
    if m > 0 and n == 0:
        for x in a:
            if ord(x) <= 90:
                return 'NO'
        return 'YES'

    S = [[-1]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        S[i][0] = 0
    for i in range(n+1):
        S[0][i] = 0

    # print_matrix(S, a)

    result = None
    is_lower_exist = False
    a_upper_cnt = 0
    b_upper_cnt = 0
    for i in range(1, m+1):
        upper_exist = None
        if ord(a[i-1]) <= 90:
            a_upper_cnt += 1
        b_upper_cnt = 0
        for j in range(1, n+1):
            if ord(b[j-1]) <= 90:
                b_upper_cnt += 1
            # if ord(a[i-1]) <= 90:
            #     print(">>>>", b[j-1])
            if ord(b[j-1]) >= 97:
                is_lower_exist = True
            if b[j-1] == a[i-1] or (b[j-1] == str(a[i-1]).upper()):
                S[i][j] = 1 + S[i - 1][j - 1]
                if ord(a[i-1]) <= 90:
                    upper_exist = True
            else:
                S[i][j] = max(S[i][j-1], S[i-1][j])
        if upper_exist is None and ord(a[i-1]) <= 90:
            # print(a[i-1], "_________", i, i-1)
            result = 'NO'

    if a_upper_cnt > b_upper_cnt:
        return 'NO'

    # print("  -", " ".join(list(b)))
    # print_matrix(S, a)
    if result is not None:
        return result
    if is_lower_exist and (m != n):
        return 'NO'
    if n == S[m][n]:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
