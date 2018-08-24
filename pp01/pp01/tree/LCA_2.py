# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def lca(root, v1, v2):
    # Enter your code here
    if root is None:
        nd = Node(None)
        nd.left = 0
        nd.right = 0
        return nd
    l = lca(root.left, v1, v2)
    r = lca(root.right, v1, v2)
    val = Node(None)
    val.left = max(l.left, r.left)
    val.right = max(l.right, r.right)
    val.info = l.info if l.info else r.info
    if root.info == v1:
        val.left = 1
    if root.info == v2:
        val.right = 1
    if val.left and val.right and val.info is None:
        val.info = root.info
    return val
