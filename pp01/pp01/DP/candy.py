#!/bin/python

import sys
def candies(n, arr):
    candies = [1]*n
    previous_rating = arr[0]
    for i in range(1,n):
        if arr[i] > previous_rating:
            candies[i] = candies[i-1]+1
        previous_rating = arr[i]
    previous_rating = arr[n-1]

    # print(arr)
    # print(candies)
    for i in range(1,n):
        j = (n-1) - i
        if arr[j] > previous_rating:
            if candies[j] <= candies[j+1]:
                candies[j] = candies[j+1] + 1
        previous_rating = arr[j]
    # print(candies)
    return sum(candies)

    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = int(raw_input().strip())
        arr.append(arr_t)
    result = candies(n, arr)
    print result
