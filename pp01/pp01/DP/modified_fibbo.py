#!/bin/python

import sys

def fibonacciModified(t1, t2, n):
    cache = {1: t1, 2: t2}
    if cache.get(n):
        return cache[n]
    else:
        for i in range(3,n+1):
            cache[i] = cache[i-2]+ cache[i-1]*cache[i-1]
        return cache[n]
    # Complete this function

if __name__ == "__main__":
    t1, t2, n = raw_input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print result
