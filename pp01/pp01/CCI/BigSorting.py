#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the bigSorting function below.
#
def bigSorting(unsorted):
    # print(unsorted)
    return sorted(unsorted)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    n = int(raw_input())

    unsorted = []

    for _ in xrange(n):
        unsorted_item = raw_input()
        unsorted.append(long(unsorted_item))

    result = bigSorting(unsorted)

    for x in result:
        print(x)

