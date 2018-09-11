#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    queries = sorted(queries, key=(lambda x: x[0]))
    max_so_far = queries[0][2]
    previous_seg = (0, 0, 0)
    m = len(queries)
    for i in range(1,m):
        current_seg = queries[i]
        if queries[i-1][0]<=current_seg[0]<=queries[i-1][1] and previous_seg[0]<=current_seg[0]<=previous_seg[1]:
            previous_seg=(max(current_seg[0], previous_seg[0], queries[i-1][0]),
                          min(current_seg[1], previous_seg[1], queries[i-1][1]),
                          previous_seg[2]+current_seg[2]
                          )
            if previous_seg[2] > max_so_far:
                max_so_far = previous_seg[2]
            # print(previous_seg)
        elif queries[i-1][0]<=current_seg[0]<=queries[i-1][1]:
            previous_seg = (max(current_seg[0], queries[i - 1][0]),
                            min(current_seg[1], queries[i - 1][1]),
                            current_seg[2] + queries[i - 1][2]
                            )
            # print(previous_seg)
            if previous_seg[2] > max_so_far:
                max_so_far = previous_seg[2]
        else:
            previous_seg = (0,0,0)
            if queries[i][2] > max_so_far:
                max_so_far = queries[i][2]
    if queries[m-1][2] > max_so_far:
        max_so_far = queries[m-1][2]
    return max_so_far


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
