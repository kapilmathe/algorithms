"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

d = Node(40)
c = Node(30, d)
b = Node(20, c)
a = Node(10, b)
t = Node(50, b)

def has_cycle(head):
    node_map = {}
    if head is None:
        return 0
    else:
        while head:
            if node_map.get(head):
                return 1
            else:
                node_map[head] = 1
                head = head.next
        # print(node_map)
        return 0

print(has_cycle(a))