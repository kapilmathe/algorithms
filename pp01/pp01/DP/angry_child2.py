# https://www.hackerrank.com/challenges/angry-children-2/problem
#!/bin/python3

import math
import os
import random
import re
import sys
INT_MAX = sys.maxsize

# Complete the angryChildren function below.
def array_avg(arr):
    return int(sum(arr)/len(arr))

def unfairness(arr):
    n = len(arr)
    w = 0
    for i in range(n-1):
        for j in range(i+1, n):
            w += abs((arr[i]-arr[j]))
    return w


def angryChildren(k, packets):
    packets.sort()
    n = len(packets)
    if k >= n:
        return unfairness(packets)
    else:
        start = 0
        end = k
        min_deviation = INT_MAX
        array_sum = sum(packets[start:end])
        for i in range(n-k):
            min = packets[i]
            max = packets[i+k-1]
            sub_avg = array_sum/k
            if i > 0:
                array_sum -= packets[i-1]
                array_sum += max
                sub_avg = array_sum/k
            current_deviation = (abs(min-sub_avg)+abs(sub_avg-max))/k
            if current_deviation < min_deviation:
                min_deviation = current_deviation
                start = i
                end = i+k

        result = unfairness(packets[start:end])
        return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    packets = []

    for _ in range(n):
        packets_item = int(input())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
