# https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next_right = None

    def __str__(self):
        if self.next_right:
            return "{0}-->{1}".format(self.val, self.next_right.val)
        else:
            return "{0}-->None".format(self.val)

def level_order(root):
    from collections import deque
    if root:
        st = deque()
        st.append(root)
        while len(st):
            start = st.popleft()
            print(start, end=' | ')
            # print(start)
            if start.left:
                st.append(start.left)
            if start.right:
                st.append(start.right)


root = node(10)
root.left = node(5)
root.right = node(50)
root.left.left = node(1)
root.right.left = node(40)
root.right.right = node(100)

def connect_level_node(root):
    if root:
        st1 = [root]
        st2 = []
        current = st1
        other = st2
        previous = None

        while len(current) or len(other):
            start = current.pop()
            print(start, previous, len(current))
            if previous is not None:

                previous.next_right = start
                if len(current):
                    previous = start
                else:
                    previous = None
            else:
                if len(current):
                    previous = start
                else:
                    previous = None
            if start.left:
                other.append(start.left)
            if start.right:
                other.append(start.right)
            if len(current) == 0:
                while len(other):
                    current.append(other.pop())


level_order(root)
print("------")
connect_level_node(root)
print("------")
level_order(root)

