"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
data = []


def preOrder(root):
    if root:
        ss = [root, ]
        cur = 0
        size = 1
        data = []
        while size:
            val = ss[cur]
            size -= 1
            data.append(val.data)
            if val.left:
                ss.append(val.left)
                size += 1
            if val.right:
                ss.append(val.right)
                size += 1
            cur += 1
        print " ".join(data)

    # Write your code here
