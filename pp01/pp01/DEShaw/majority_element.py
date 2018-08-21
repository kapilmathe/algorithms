# https://practice.geeksforgeeks.org/problems/majority-element/0
from collections import Counter


def majority_element(a, n):
    elem_freq = Counter(a)
    for key, value in elem_freq.items():
        if value > n//2:
            return key
    return 'NO Majority Element'


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    print(majority_element(arr, n))

