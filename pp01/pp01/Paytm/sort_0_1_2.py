# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
from collections import Counter


def sort_012(arr):
    elem_cnt = dict(Counter(arr))
    j = 0
    for i in range(3):
        m = elem_cnt.get(i, 0)
        for _ in range(m):
            arr[j] = i
            j += 1
    return True


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    sort_012(arr)
    print(" ".join([str(x) for x in arr]))
