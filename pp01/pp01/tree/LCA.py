# A Binary Tree node
class Node:

    # Constructor to create a new tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, n1, n2):
    if root is None:
        return None
    else:
        l = lca(root.left, n1,n2)
        r = lca(root.right,n1, n2)
        if l is not None and r is not None:
            if (l == n1 and r == n2) or (l == n2 and r == n1):
                return root.data

        elif l and ((l == n1 and root.data == n2) or (l == n2 and root.data == n1)):
            return root.data
        elif r and ((r == n1 and root.data == n2) or (r == n2 and root.data == n1)):
            return root.data
        elif l is None and r is None and root.data in (n1,n2):
            return root.data

        return l if l else r


root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.left.right = Node(49)
root.left.right = Node(30)
root.right.left = Node(36)

result = lca(root, 49, 25)
print(result)