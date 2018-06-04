#!/bin/python3

import os
import sys

# Complete the substringDiff function below.
def substringDiff(k, s1, s2):
    best = 0
    n1 = len(s1)
    n2 = len(s2)
    count = [[0]*(n2+1)]*(n1+1)
    for i in range(n1):
        bad = 0
        for j in range(n2):
            if i+j >= n1:
                best = max(best, count[i][j])
                break
            if (s1[i+j] != s2[j]):
                bad += 1
            if bad > k:
                best = max(best, count[i][j])
                break

            count[i + 1][j + 1] = (0 if (s1[i+j] == s2[j]) else 1) + count[i][j]
            best = max(best, count[i][j])
    return best


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        kS1S2 = raw_input().split(' ')

        k = int(kS1S2[0])

        s1 = kS1S2[1]

        s2 = kS1S2[2]

        result = substringDiff(k, s1, s2)
        print(result)

