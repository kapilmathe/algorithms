#!/bin/python
CAP_SET = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
LOW_SER = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
import sys

def abbreviation(a, b):
    a_i = -1
    for i in range(len(b)):
        ch = b[i]
        a_i += 1
        # print(ch)
        # print(a_i)
        while (a_i < len(a)):
            # print("a[a_i]= {0}".format(a[a_i]))
            if ch.lower() == a[a_i].lower():
                break
            a_i += 1
        if a_i >= len(a):
            # print("kapil")
            return 'NO'

    a_cap = CAP_SET.intersection(a)
    # print(a_cap - set(b))
    if len(a_cap - set(b)):
        return 'NO'
    return 'YES'


    # Complete this function

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        a = raw_input().strip()
        b = raw_input().strip()
        result = abbreviation(a, b)
        print result

