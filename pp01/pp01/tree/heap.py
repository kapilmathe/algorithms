from heapq import heappush, heappop, heapify
INT_MIN = -132133523412
INT_MAX = 22133123123


class minHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)/2

    def insertKey(self, k):
        heappush(self.heap, k)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)], self.heap[i])

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]


class arrayMinHeap:
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
        while (i!=0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = (
                self.heap[i], self.heap[self.parent(i)])
            i = self.parent(i)

    def heapify_down(self, i):
        l = self.left(i)
        r = self.right(i)
        size = self.size
        smallest = i
        if (l < size and self.heap[l] < self.heap[i]):
            smallest = l
        if (r < size and self.heap[r] < self.heap[smallest]):
            smallest = r
        if (smallest != i):
            self.heap[i], self.heap[smallest] = (
                self.heap[smallest], self.heap[i]
            )
            self.heapify_down(smallest)

    def insertKey(self, data):
        i = self.heap_size()
        self.heap.append(data)
        self.heapify_up(i)
        self.size += 1

    def extractMin(self):
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
        return  self.extractMin()


    def __str__(self):
        return  ", ".join([str(x) for x in self.heap])

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


if __name__ == '__main__':

    print("endter heap size")
    n = int(raw_input().strip())
    heap = arrayMinHeap()
    for i in range(n):
        x = int(raw_input().strip())
        heap.insertKey(x)
    print("+++++++++++++++++++++++")
    print(heap)
    print(heap.size)
    print("+++++++++++++++++++++++")
    heap.decreaseKey(5, 1)
    print(heap)
    print(heap.size)
    print("+++++++++++++++++++++++")
    print(heap.deleteKey(3))
    print(heap)
    print(heap.size)
    print("+++++++++++++++++++++++")

    # print("-----------------------")
    # for i in range(n):
    #     print("min={0}".format(heap.extractMin()))
    #     print(heap)
