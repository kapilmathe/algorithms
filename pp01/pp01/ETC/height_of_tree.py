class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def update_right(self, nd):
        self.right = nd

    def update_left(self, nd):
        self.left = nd


def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(4)
root.left.left.left = Node(3)

print(height(root))