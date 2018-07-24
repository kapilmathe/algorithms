# https://www.geeksforgeeks.org/print-cousins-of-a-given-node-in-binary-tree-single-traversal/
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_child(parent, root, cousins ):
    print("ge child called: parent:{0}: other child:{1}".format(parent.data, root.data))
    if parent:
        other_child = None
        if parent.left and parent.left != root:
            other_child = parent.left
        elif parent.right and parent.right != root:
            other_child = parent.right

        cousins.append(other_child.left.data if other_child.left else None)
        cousins.append(other_child.right.data if other_child.right else None)
    print("cosuins = {0}".format(cousins))





def find_cousins(root, parent, nd, cousins):

    if root:
        print(root.data, nd, parent.data if parent else None)
        if parent:
            if root.data == nd:
                return (True, False)
            ls = find_cousins(root.left, root, nd, cousins)
            if ls[0] is not None:
                cousins = get_child(parent, root, cousins)
                return (None, None)
            rs = find_cousins(root.right, root, nd, cousins)
            if rs[0] is not None:
                cousins = get_child(parent, root, cousins)
                return (None, None)
            return (None, None)
        else:
            if root.data == nd or (root.left and root.left.data == nd) or (root.right and root.right.data == nd):
                return (None, None)
            else:
                find_cousins(root.left, root, nd, cousins)
                if len(cousins):
                    return (None, None)
                find_cousins(root.right, root, nd, cousins)
                return (None, None)
    else:
        return (None, None)



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

cousins= []
find_cousins(root, None, 14, cousins)
print(cousins)