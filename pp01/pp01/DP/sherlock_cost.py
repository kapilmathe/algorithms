#!/bin/python
from __future__ import print_function
def cost(B):
    l = len(B)
    dp  = [[0]*2 for i in range(l)]
    print(dp)
    for i in range(l-1):
        dp[i+1][0] = max(dp[i][0], dp[i][1]+abs(B[i]-1))
        dp[i+1][1] = max(dp[i][0]+abs(B[i+1]-1), dp[i][1]+abs(B[i]-B[i+1]))
    print(dp)
    return max(dp[n-1][0],dp[n-1][1])


if __name__ == '__main__':

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        B = map(int, raw_input().rstrip().split())

        result = cost(B)

        print(result)
