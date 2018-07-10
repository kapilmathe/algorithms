#!/bin/python3
# https://www.hackerrank.com/challenges/construct-the-array/problem?h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys
def print_matrix(a):
    for l in a:
        print(" ".join([str(x) for x in l]))


def f_way_dp(arr, start, n, k):
    s = [None] * n
    s[n - 1] = 0
    s[0] = 0

    def f_way(arr, start, n, k):
        # print(arr, start, n, k)
        if s[start] is not None:
            return s[start]
        else:
            if arr[start] != 0:
                return 0
            if start >= (n - 1):
                return 0
            total_way = 0
            for i in range(1, k + 1):

                if arr[start - 1] == i or arr[start + 1] == i:
                    continue
                else:
                    print(i)
                    arr[start] = i
                    if s[start + 1] is not None:
                        total_way += (s[start + 1] + 1)
                    else:
                        print(arr)
                        s[start + 1] = f_way(arr, start + 1, n, k)
                        total_way += (s[start + 1] + 1)
            s[start] = total_way
            # arr[start] = 0
            return s[start]

    result = f_way(arr, start, n, k)
    return result


# Complete the countArray function below.
INT_MAX = int(7+math.pow(10,9))
def f_way(arr, start, n, k, x, prev, next, s):
    if s[start][prev] is not None:
        return s[start][prev]
    else:
        # print("(",start,prev, ")")
        # print(s)
        if start == n - 2:
            next = x
        # print(arr, start, n, k)
        if arr[start] != 0:
            s[start][prev] = 0
            return s[start][prev]
        if start >= (n - 1):
            s[start][prev] = 0
            return s[start][prev]
        total_way = 0
        for i in range(1, k + 1):

            if prev == i or next == i:
                continue
            else:
                # print(">>>", start, ">>>>", i)
                arr[start] = i
                if start == n - 2:
                    total_way += 1
                else:
                    # print(start+1, i)
                    if s[start + 1][i] is not None:
                        total_way += s[start + 1][i]
                    else:
                        s[start + 1][i] = f_way(arr, start + 1, n, k, x, i, 0, s)
                        total_way += s[start + 1][i]
                # print(">>total_count=", total_way,arr)
        arr[start] = 0
        s[start][prev] = int(total_way%INT_MAX)
        return s[start][prev]


def countArray(n, k, x):
    arr = [0] * n
    start = 1
    arr[0] = 1
    arr[n - 1] = x
    s = [[None] * (k+1) for i in range(n)]
    cnt = f_way(arr, start, n, k, x, prev=1, next=arr[start + 1], s=s)
    print_matrix(s)
    return cnt
    # Return the number of ways to fill in the array.


if __name__ == '__main__':
    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    print(answer)
