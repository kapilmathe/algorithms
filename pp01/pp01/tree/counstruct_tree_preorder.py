INT_MAX = 999999999
INT_MIN = -999999999

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val, end=", ")
        preorder(root.left)
        preorder(root.right)


def construct_bst(A):
    n = len(A)
    def preorder_bst_build(a, a_index_ref, key, min, max, n):
        if a_index_ref[0] >= n:
            return None

        nd = None
        if key > min and key < max:
            nd = node(key)
            a_index_ref[0] += 1
            if a_index_ref[0] < n:
                nd.left = preorder_bst_build(a, a_index_ref, a[a_index_ref[0]], min, nd.val, n)
                nd.right = preorder_bst_build(a, a_index_ref, a[a_index_ref[0]], nd.val, max, n)
        return nd

    root = preorder_bst_build(A, [0], A[0], INT_MIN, INT_MAX, n)
    return root


a = [10, 5, 1, 40, 50]
root = construct_bst(a)
preorder(root)

