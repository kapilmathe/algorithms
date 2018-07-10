#!/bin/python

import math
import os
import random
import re
import sys

# Complete the equal function below.

def equal(arr):
    n = len(arr)
    min_candy = min(arr)
    s = [0]
    for j in range(1):
        s[j] = 0
        for i in range(n):
            extra_candy = abs(arr[i] - (min_candy -j))
            s[j] += (extra_candy//5 + (extra_candy%5)//2 + (extra_candy%5)%2)
    # print(s)
    min_round = min(s)
    return min_round


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        result = equal(arr)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
