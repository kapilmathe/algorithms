class Node:

    # Constructor to create a new tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def vertical_sum_outer(r):
    vtl_sum = {}
    def vertical_sum(root, position):
        if root:
            if vtl_sum.get(position):
                vtl_sum[position] += root.data
            else:
                vtl_sum[position] = root.data
            vertical_sum(root.left, position-1)
            vertical_sum(root.right, position+1)
    vertical_sum(r, 0)
    return vtl_sum

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    vs = vertical_sum_outer(root)
    print(vs)