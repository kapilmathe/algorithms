#!/bin/python

import sys


class Athlete:
    def __init__(self, attributes, id):
        self.attributes = attributes
        self.id = id

    def __repr__(self):
        return " ".join([str(x) for x in self.attributes])


def cmp_athlete(k):
    def cmp(Athelet1, Athelet2):
        global k
        if Athelet1.attributes[k] - Athelet2.attributes[k] == 0:
            return Athelet1.id - Athelet2.id
        else:
            return Athelet1.attributes[k] - Athelet2.attributes[k]

    return cmp


if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    i = 0
    for arr_i in xrange(n):
        i += 1
        arr_temp = map(int, raw_input().strip().split(' '))
        ath = Athlete(arr_temp, i)
        arr.append(ath)
    k = int(raw_input().strip())
    result = sorted(arr, cmp=cmp_athlete(k))
    for r in result:
        print(r)
