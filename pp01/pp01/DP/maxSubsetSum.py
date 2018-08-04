#!/bin/python3

import os


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    S = [None] * (n + 1)
    S[0] = 0

    def maxSubsetSumTD(arr, n):
        if n <= 0:
            return 0
        if S[n]:
            return S[n]
        else:
            S[n - 1] = maxSubsetSumTD(arr, n - 1)
            S[n - 2] = maxSubsetSumTD(arr, n - 2)
            S[n] = max(S[n - 1], arr[n - 1] + S[n - 2])
            return S[n]

    def maxSubsetSumBU(arr, n):
        if n > 0:
            S[1] = max(S[0], arr[0])
            if S[n]:
                return S[n]
            for i in range(2, n + 1):
                S[i] = max(S[i - 1], arr[i - 1] + S[i - 2])
            return S[n]
        else:
            return 0

    result = maxSubsetSumBU(arr, n)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
