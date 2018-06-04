#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the absolutePermutation function below.
#
def absolutePermutation(n, k):
    perm = [0]*n
    num_map = {x:1 for x in range(1,n+1)}
    # print(num_map)
    # print(range(1,n+1))
    for i in range(1,n+1):
        val = k+i
        val2 = i-k
        if num_map.get(val):
            perm[i-1] = val
            del num_map[val]
        elif num_map.get(val2):
            perm[i-1] = val2
            del  num_map[val2]
        else:
            return -1
    print(num_map)
    return perm

if __name__ == '__main__':
    t = int(raw_input())
    for t_itr in xrange(t):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)
        if result != -1:
            print(" ".join(map(str,result)))
        else:
            print(-1)