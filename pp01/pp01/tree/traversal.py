from random import *
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def fixPrevPtr(root):
    if root is not None:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root
        fixPrevPtr(root.right)
        
def inOrderTraversalDLL(root, parent=None):
    if root:
        inOrderTraversalDLL(root.left, root)
        root.left = parent
        inOrderTraversal(root.right)

        # print(root.data)
        # if root.right is None:
        #     parent.right
        # inOrderTraversal(root.right)

def inOrderTraversal(root):
    a,b = None, None
    if root:
        inOrderTraversal(root.left,)
        print(root.data)
        inOrderTraversal(root.right,)


def preOrderTraversal(root):
    if root:
        print(root.data)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
        print(root.data)

def zigzag(root):
    st1 = []
    st2 = []
    current_st = st1
    hold_st = st2
    current_st.append(root)
    direction = True
    while len(st1) or len(st2):
        current = current_st.pop()
        print(current.data)
        if direction:
            if current.left:
                hold_st.append(current.left)
            if current.right:
                hold_st.append(current.right)
        else:
            if current.right:
                hold_st.append(current.right)
            if current.left:
                hold_st.append(current.left)
        if len(current_st) == 0:
            direction = not(direction)
            temp = current_st
            current_st = hold_st
            hold_st = temp

def build_bst(data, root):
    if root is None:
        root = node(data)
        return root
    root_val = root.data
    if data >= root_val:
        if root.right is None:
            l = node(data)
            root.right = l
        else:
            build_bst(data, root.right)
        return root
    else:
        if root.left is None:
            l = node(data)
            root.left = l
        else:
            build_bst(data, root.left)
        return root

n = int(raw_input().strip())
root = None

def build_tree(root, nd):
    if root:
        if root.left is None:
            root.left = nd
        elif root.right is None:
            root.right = nd
        else:
            build_tree(root.left, nd)
    else:
        root = nd

    return root

for a0 in xrange(n):
    data =  int(raw_input().strip())
    # print data
    nd = node(data)
    root = build_tree(root, nd)
    # root = build_bst(data, root)

# zigzag(root)
print("::")
a = inOrderTraversalDLL(root, None)
print a
print(":::::")
cnt = 0
x = root
while  cnt < 10:
    print(x.data if x else "None")
    x = x.left if x and x.left else x and x.right
    cnt += 1


# print(a.data)
# preOrderTraversal(root)
# print("::")
# postOrderTraversal(root)