#!/bin/python
INT_MIN = -132133523412
INT_MAX = 22133123123
class arrayMaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def heap_size(self):
        self.size = len(self.heap)
        return self.size

    def parent(self, i):
        return (i-1)/2

    def left(self, i):
        return (2*i+1)

    def right(self, i):
        return (2*i+2)

    def heapify_up(self, i):
        while (i!=0 and self.heap[self.parent(i)] < self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = (
                self.heap[i], self.heap[self.parent(i)])
            i = self.parent(i)

    def heapify_down(self, i):
        l = self.left(i)
        r = self.right(i)
        size = self.size
        highest = i
        if (l < size and self.heap[l] > self.heap[i]):
            highest = l
        if (r < size and self.heap[r] > self.heap[highest]):
            highest = r
        if (highest != i):
            self.heap[i], self.heap[highest] = (
                self.heap[highest], self.heap[i]
            )
            self.heapify_down(highest)


    def insertKey(self, data):
        i = self.heap_size()
        self.heap.append(data)
        self.heapify_up(i)
        self.size += 1

    def extractMax(self):
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        if self.size > 1:
            lastelm = self.heap.pop()
            elementrtn = self.heap[0]
            self.size -= 1
            self.heap[0] = lastelm
            self.heapify_down(0)
            return elementrtn
        return None

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        self.heapify_up(i)

    def deleteKey(self, i):
        self.decreaseKey(i, INT_MIN)
        return  self.extractMax()


    def __str__(self):
        return  ", ".join([str(x) for x in self.heap])
import sys
S = [1,3,5]

def closest_number(i):
    closest = S[0]
    val = i - closest
    for c in S[1:]:
        if (i-c) >= 0 and (i-c) < val:
            closest = c
    return closest

def dp_equal(maxHeap):
    while(equal_array(maxHeap.heap)):
        if equal_array(maxHeap.heap):
            return 0
        max_val = maxHeap.heap[0]
        min_val = min(maxHeap.heap[maxHeap.left(0)], maxHeap.heap[maxHeap.right(0)])
        diff = max_val - min_val
        op_number = closest_number(diff)
        # print("op_number={0}".format(op_number))
        cnt = diff/op_number
        # print("cnt={0}".format(cnt))
        for i in range(cnt):
            for j in range(1,maxHeap.size):
                new_val = maxHeap.heap[j]+op_number
                maxHeap.decreaseKey(j,new_val)
        # print(maxHeap.heap)
        cnt += dp_equal(maxHeap)
    return cnt


def equal_array(arr):
    if len(arr):
        val = arr[0]
        for x in arr:
            if x != val:
                return False
        return True
    return True


def equal(arr):
    maxHeap = arrayMaxHeap()
    val = arr[0]
    flag = True
    for x in arr:
        if x != val:
            flag = False
        maxHeap.insertKey(x)

    # print(maxHeap)
    if flag:
        return 0
    else:
        cnt = dp_equal(maxHeap)
        return cnt
    # Complete this function

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = equal(arr)
        print result

