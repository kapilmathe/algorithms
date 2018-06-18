class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 10 5 50 1 40 100
root = node(10)
root.left = node(5)
root.right = node(50)
root.left.left = node(1)
root.right.left = node(40)
root.right.right = node(100)

def bst_rs(root,l,h):
    if root is None:
        return 0
    if root.val == l and root.val == h:
        return 1
    else:
        if root.val <l:
            return bst_rs(root.right, l, h)
        if root.val >h:
            return bst_rs(root.left, l, h)
        else:
            return 1 + bst_rs(root.left, l, h) + bst_rs(root.right, l, h)


print(bst_rs(root, 10,10))