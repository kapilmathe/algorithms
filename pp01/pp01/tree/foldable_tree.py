class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root, l):
    if root:
        l.append("X")
        # print(root.data, end=" ")
        inOrder(root.left, l)
        inOrder(root.right, l)
    else:
        # print("N")
        l.append("N")

def inOrder2(root, l2):
    if root:
        l2.append("X")
        inOrder2(root.right, l2)
        inOrder2(root.left, l2)
    else:
        # print("N")
        l2.append("N")

def foldable_binary_tree(root):
    if root:
        l_subtree = []
        r_subtree = []
        inOrder(root.left, l_subtree)
        inOrder2(root.right, r_subtree)
        if (l_subtree) == (r_subtree):
            return "Yes"
        return "No"




root = node(14)
root.left = node(12)
root.right = node(18)
root.left.left = node(8)
root.left.right = node(13)
root.right.left = node(16)
root.right.right = node(26)
root.right.right.left = node(25)
root.right.right.right = node(29)
root.left.left.left = node(11)
root.left.left.right = node (122)

root.left.left.left.right = node(9)
root.right.right.right.left = node(10)

l0 = []
inOrder(root.left, l0)
print(l0)
l2 = []
inOrder2(root.right, l2)
print(l2)

if l0 == l2:
    print("YES")

# root.left, root.right =
# print(l0)
# l = []
# inOrder(root.left, l)
# print(l)