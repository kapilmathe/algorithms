#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stockmax function below.
def stockmax(prices):
    n = len(prices)
    highest_sofar = prices[n - 1]
    highest_index = n - 1
    profit = 0
    for i in range(n - 2, -1, -1):
        current_index = i
        if prices[current_index] > highest_sofar:
            if highest_index > current_index + 1:
                print(highest_index, current_index+1)
                profit += highest_sofar * (highest_index - current_index - 1) - sum(
                    prices[current_index + 1:highest_index])
                print(profit)
            highest_sofar = prices[current_index]
            highest_index = current_index
    profit += highest_sofar * (highest_index - 0) - sum(prices[0:highest_index])
    return profit


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
