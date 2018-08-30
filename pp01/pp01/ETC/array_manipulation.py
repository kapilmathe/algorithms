# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    queries = sorted(queries, key=(lambda x: x[0]))
    m =len(queries)
    # print(queries)
    max_so_far = queries[0][2]
    current_sum = queries[0][2]
    previous_range = queries[0]
    for i in range(1,m):
        current_range = queries[i]
        if previous_range[0] <=current_range[0] <= previous_range[1]:
            previous_range = (current_range[0]




    return 0


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(tuple(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
