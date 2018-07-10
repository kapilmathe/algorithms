#!/bin/python

import sys
import math
def countArray(n, k, x):
    available_no = set(range(1,k))
    extream = {1, x}
    arr = [0]*n
    diff  = 1
    cnt = 0
    if n == 3:
        possible_number = available_no - extream
        return len(possible_number)
    else:
        return int((math.pow((k-1), (n-2)) - (k-2))%(7+math.pow(10,9)))

    # Return the number of ways to fill in the array.

if __name__ == "__main__":
    n, k, x = input().strip().split(' ')
    n, k, x = [int(n), int(k), int(x)]
    answer = countArray(n, k, x)
    print(answer)
