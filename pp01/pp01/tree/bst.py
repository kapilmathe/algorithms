class BST:
    def __init__(self):
        self.data = []
        self.size = 0

    def left(self, i):
        if 2*i+1 >= self.size:
            return None
        else:
            return 2*i+1

    def right(self, i):
        if (2*i+2) >= self.size:
            return None
        else:
            return 2*i+2

    def parent(self, i):
        if i > 0:
            if i%2:
                return i/2
            else:
                return (i-1)/2
        else:
            return None


    def find_index(self, val):
        root = 0
        if self.size > 0:
            while root is not None:
                start_val = self.data[root]
                if start_val == val:
                    return root
                elif start_val > val:
                    root = self.left(root)
                elif start_val < val:
                    root = self.right(root)
        return None


    def add(self, val):
        # if self.size == 0:
        self.data.append(val)
        self.size += 1
        # return val
        # start = self.data[0]
        # i = 0
        # j = 0
        # while j is not None:
        #     i = j
        #     if val < start:
        #         # left child
        #         j = self.left(i)
        #         if j is None:
        #
        #     else:
        #         # right child
        #         j = self.right(i)

def inOrder(bst, root):
    if root:
        inOrder(bst, bst.left(root))
        print(bst.data[root])
        inOrder(bst, bst.right(root))

def find_nge(bst, key):
    index = bst.find_index(key)
    print("key index={0}".format(index))
    if index is not None:
        if bst.right(index):
            start  = bst.right(index)
            print("right={0}".format(start))
            while start:
                val = bst.data[start]
                start = bst.left(start)
            return val
        else:
            start = bst.parent(index)
            print("parent={0}".format(start))
            val = None
            while start is not None:
                print("parent={0}".format(start))
                val = bst.data[start]
                if val > key:
                    return val
                start = bst.parent(start)
    return None


if __name__ == '__main__':
    n = int(raw_input().strip())
    bst = BST()
    for i in range(n):
        data = int(raw_input().strip())
        bst.add(data)

    print("::")
    print(bst.data)
    print(bst.size)
    c = 1
    while c:
        c = int(raw_input().strip())
        nge = find_nge(bst, c)
        print(nge)

