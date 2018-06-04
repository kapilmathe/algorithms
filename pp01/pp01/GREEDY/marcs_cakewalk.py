#!/bin/python

import sys
import math

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    result = 0
    for i in range(len(calorie)):
        result += math.pow(2,i)*calorie[i]
    return long(result)

if __name__ == "__main__":
    n = int(raw_input().strip())
    calorie = map(int, raw_input().strip().split(' '))
    result = marcsCakewalk(calorie)
    print result
