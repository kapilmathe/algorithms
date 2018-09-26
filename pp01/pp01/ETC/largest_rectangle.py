#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    n = len(h)
    temp = []
    max_so_far = -1
    current_min_bar = h[0]
    length_so_far = 0
    start = -1
    end = -1
    for i in range(n):
        curr_area = h[i]
        if curr_area > max_so_far:
            max_so_far = curr_area
            length_so_far = 1
            start = i
            end = i
            if current_min_bar > h[i]:
                current_min_bar = h[i]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
