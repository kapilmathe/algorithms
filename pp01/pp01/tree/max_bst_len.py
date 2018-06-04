INT_MIN = -543543443243243
INT_MAX = 543543443243243

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_bst(root):
    if root:
        print(root.data)
        l = max_bst(root.left)
        r = max_bst(root.right)
        print("{1}=l={0}".format(l, root.data,))
        print("{1}=r={0}".format(r, root.data,))
        if l[0] is False or r[0] is False:
            return [False, max(l[1], r[1]), min(l[2], r[2]), max(l[3], r[3])]
        else:
            is_bst = True
            val = root.data
            if l[1] == r[1] == 0:
                return [True, 1, val, val]
            if val <= l[3] and l[1] > 0:
                is_bst = False
            if val >= r[2] and r[1] > 0:
                is_bst = False
            if is_bst:
                return [True, l[1]+r[1]+1, min(l[2], r[2], root.data), max(l[3], r[3], root.data )]
            else:
                return [False, max(l[1], r[1]), 0, 0]
    else:
        return [True, 0, INT_MAX, INT_MIN]

# n = int(raw_input().strip())

root = node(14)
root.left = node(12)
root.right = node(18)
root.left.left = node(8)
root.left.right = node(13)
root.right.left = node(16)
root.right.right = node(26)
root.right.right.right = node(29)
root.right.right.left = node(25)

print(max_bst(root))
            