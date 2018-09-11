# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the triplets function below.
def find_index(arr, val, start, end):
    # print(arr, val, start, end)
    if start > end:
        return start
    if start == end:
        if arr[start] <= val:
            return (start + 1)
        else:
            return start
    else:
        mid = (start + end) // 2
        if arr[mid] <= val:
            return find_index(arr, val, mid + 1, end)
        else:
            return find_index(arr, val, start, mid)


def triplets(a, b, c):
    s_a = sorted(list(set((a))))
    s_b = sorted(list(set((b))))
    s_c = sorted(list(set((c))))
    len_a = len(s_a)
    len_c = len(s_c)
    cnt = 0
    i = 0
    j = 0
    for x in s_b:
        i = find_index(s_a, x, i, len_a - 1)
        j = find_index(s_c, x, j, len_c - 1)
        cnt += (i * j)
    return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().strip().split()))

    ans = triplets(arra, arrb, arrc)

    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()
