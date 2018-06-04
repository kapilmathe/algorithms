class node:
    def __init__(self, val, nd=None):
        self.data = val
        self.next = nd

def print_linklist(head):
    if head:
        start = head
        while start is not None:
            print "%d\t"% (start.data)
            start = start.next

def reverse_linked_list(head, k):
    if head:
        start = head
        prev = None
        new_head = None
        counter = 0
        st = []
        while start is not None:
            counter += 1
            if counter < k:
                st.append(start)
                start = start.next
            else:
                st.append(start)
                start = start.next
                while counter:
                    nd = st.pop()
                    counter -= 1
                    if prev is not None:
                        prev.next = nd
                        prev = nd
                        prev.next = None
                    else:
                        prev = nd
                        if new_head is None:
                            new_head = nd
        if len(st):
            while len(st):
                nd = st.pop()
                if prev is not None:
                    prev.next = nd
                    prev = nd
                    prev.next = None
                else:
                    prev = nd
                    if new_head is None:
                        new_head = nd
        return new_head
    else:
        return None


if __name__ == '__main__':
    head = node(80)
    a = node(70, head)
    b = node(60, a)
    c = node(50, b)
    d = node(40, c)
    e = node(30, d)
    f = node(20, e)
    g = node(10, f)
    print_linklist(g)
    new_head = reverse_linked_list(g, 3)
    print("::")
    print_linklist(new_head)