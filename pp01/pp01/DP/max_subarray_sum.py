#!/bin/python

import sys

def max_subarray(A):
    start = None
    end = None
    max_ending_here = max_so_far = A[0]
    for x in range(1, len(A)):
        max_ending_here += A[x]
        if max_ending_here < 0:
            max_ending_here = 0
            start = x+1
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = x
        max_so_far = max(max_so_far, max_ending_here)
    return start, end, max_so_far

# def maxSubarrayDP():
#     dp = {}
#     def maxSubarray(arr):
#         n = len(arr)
#         subarray_sum = 0
#         items = 0
#         for i in range(n):
#             if arr[i] >= 0:
#                 subarray_sum += arr[i]
#                 items += 1
#             else: 
#                 dp[i+1] =dp.get(i+1) if dp.get(i+1) else maxSubarray(arr[i + 1:n])
#                 s11 = dp[i+1]
#                 s1 = subarray_sum + arr[i] + s11[0]
#                 s2 = s11[0]
#                 if s1 > s2 and s1 >subarray_sum:
#                     subarray_sum = s1
#                     items += 1+s11[1]
#                 elif s2 > s1 and s2 > subarray_sum:
#                     subarray_sum = s2
#                     items = s2[1]
#                 else:
#                     subarray_sum = subarray_sum
#                 if items:
#                     return (subarray_sum, items)
#                 else:
#                     max = arr[0]
#                     for x in arr:
#                         if x >= max:
#                             max = x
#                             items = 1
#                     return (max, items)
#         return (subarray_sum, items)
#         # Complete this function
#     return maxSubarray

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = A= [-2,-3, 4, -1, -2, 1, 5, -3] # [int(x) for x in input().strip().split(' ')]
        # subsequence_sum = 0
        # subsequence_item = 0
        # for i in range(n):
        #     if arr[i] >= 0:
        #         subsequence_sum += arr[i]
        #         subsequence_item += 1
        # if not subsequence_item:
        #     max_elem = arr[0]
        #     for x in arr:
        #         if x >= max_elem:
        #             max_elem = x
        #             subsequence_item = 1
        #     subsequence_sum = max_elem
        # # dpresult= maxSubarrayDP()
        # # result = dpresult(arr)
        result = max_subarray(arr)
        print(result)
        # print(" ".join(map(str, (result, subsequence_sum))))
# A= [-2,-3, 4, -1, -2, 1, 5, -3]