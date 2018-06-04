#!/bin/python

from __future__ import print_function

import os
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(n, ar):
    bird_map = {}
    highest_cnt = 0
    bird_id = None
    for x in ar:
        if bird_map.get(x):
            bird_map[x] += 1
            if highest_cnt < bird_map[x]:
                highest_cnt = bird_map[x]
                bird_id = x
        else:
            bird_map[x] = 1
            if highest_cnt < bird_map[x]:
                highest_cnt = bird_map[x]
                bird_id = x
    print(bird_map)
    return bird_id


if __name__ == '__main__':
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())
    result = migratoryBirds(n, ar)
    print(result)