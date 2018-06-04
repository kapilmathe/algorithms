class node:
    def __init__(self, val, nd=None):
        self.data = val
        self.next = nd

def printList(root):
    while (root != None):
        print "%d" % (root.data),
        root = root.next

def linked_list_sum(a,b):
    if a is None or b is None:
        return a if b is None else b
    else:
        prev = None
        head = None
        a_start = a
        b_start = b
        co = 0
        while (a_start!=None or b_start!=None):
            a_val = a_start.data if a_start else 0
            b_val = b_start.data if b_start else 0
            val = a_val + b_val + co
            co = val/10
            nd = node(val%10)
            if prev is not None:
                prev.next = nd
                prev = nd
            else:
                prev = nd
                if head is None:
                    head = nd
            a_start = a_start.next if a_start else None
            b_start = b_start.next if b_start else None
        if co:
            nd = node(co)
            prev.next = nd
        return head


if __name__ == '__main__':
    head = node(5)
    a = node(4, head)
    b = node(3, a)

    c = node(5)
    d = node(4, c)
    e = node(3, d)

    printList(b)
    print("\n")
    printList(e)
    head = linked_list_sum(b,e)
    print("\n")
    printList(head)
    # f = node(2, e)
    # g = node(1, f)
    #