#!/bin/python3
#https://www.hackerrank.com/challenges/construct-the-array/problem?h_r=next-challenge&h_v=zen
import math
import os
import random
import re
import sys

# Complete the countArray function below.

def f_way(arr, start, n, k, x, prev, next):
    print("(",start,prev, ")")
    if start == n-2:
        next = x
    # print(arr, start, n, k)
    if arr[start] != 0:
        return 0
    if start >= (n - 1):
        return 0
    total_way = 0
    for i in range(1, k + 1):

        if prev == i or next == i:
            continue
        else:
            # print(">>>", start, ">>>>", i)
            arr[start] = i
            if start == n-2:
                total_way += 1
            else:
                total_way += (f_way(arr, start + 1, n, k, x, i, 0))
            # print(">>total_count=", total_way,arr)
    arr[start] = 0
    return total_way

def f_way_dp(arr, start, n ,k):
    s  = [None]*n
    s[n-1] = 0
    s[0] = 0
    def f_way(arr, start, n, k):
        # print(arr, start, n, k)
        if s[start] is not None:
            return s[start]
        else:
            if arr[start]!=0:
                return 0
            if start>= (n-1):
                return 0
            total_way = 0
            for i in range(1,k+1):

                if arr[start-1] == i or arr[start+1]==i:
                    continue
                else:
                    print(i)
                    arr[start] = i
                    if s[start+1] is not None:
                        total_way += (s[start+1]+1)
                    else:
                        print(arr)
                        s[start+1] = f_way(arr, start+1,n,k)
                        total_way += (s[start+1] + 1)
            s[start] = total_way
            # arr[start] = 0
            return s[start]
    result= f_way(arr,start,n,k)
    return result

def countArray(n, k, x):
    arr = [0]*n
    start = 1
    arr[0] = 1
    arr[n-1] = x
    cnt = f_way(arr, start, n, k, x, prev=1, next=arr[start+1])
    return cnt
    # Return the number of ways to fill in the array.

if __name__ == '__main__':

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    print(answer)
