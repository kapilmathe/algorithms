#!/bin/python
INT_MIN = float('-inf')# -22133123123323
INT_MAX = float('inf')
import sys

def minimumAbsoluteDifference(n, arr):
    min = INT_MAX
    for x in arr:
        if min > x:
            min = x
    if min < 0:
        for i in range(n):
            arr[i] += abs(min)

    arr.sort()
    min_diff = INT_MAX
    for i in range(n-1):
        diff = abs(arr[i+1] - arr[i])
        if min_diff > diff:
            min_diff = diff
    return min_diff


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = minimumAbsoluteDifference(n, arr)
    print result