# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_move = [(-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]
    max_sofar = -sys.maxsize
    max_sofar_center = (-1, -1)
    for i in range(1,5):
        for j in range(1,5):
            center = (i,j)
            hourglass_sum = 0
            for x_move, y_move in hourglass_move:
                hourglass_sum += arr[i+x_move][j+y_move]
            if hourglass_sum > max_sofar:
                max_sofar = hourglass_sum
                max_sofar_center = center

    return max_sofar


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
