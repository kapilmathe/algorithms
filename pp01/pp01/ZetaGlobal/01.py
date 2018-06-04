# Enter your code here. Read input from STDIN. Print output to STDOUT

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# k = 2
# 3 -> 4 -> 1 -> 2 -> 5 -> 6
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# 3 -> 4 -> 1 -> 2 -> 7 -> 8 -> 5 -> 6

# k = 3
# 4 -> 5 -> 6 -> 1 -> 2 -> 3


# n = ?, k = ?
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def change_next(self, node):
        self.next = node


class linked_list:
    def __init__(self, start, end):
        self.head = start
        self.tail = end


def swap_ll(head, n, k):
    if n / k < 2:
        return head
    else:
        new_head = None
        new_tail = None
        previous_head = head
        start = previous_head
        previous_tail = None
        counter = 0
        first_iteration = True
        pair_cnt = 0
        ll_list = []
        overall_counter = 0
        while start is not None:
            counter += 1
            if counter == k:
                counter = 0
                overall_counter += 1
                ll = linked_list(start=previous_head, end=start)
                ll_list.append(ll)
                start = start.next
                previous_head = start
            else:
                start = start.next
            if overall_counter == (n / k):
                if start and start.next is None:
                    ll = linked_list(start=previous_head, end=start)
                    ll_list.append(ll)
                    break
                else:
                    pass

        pair_start = 0
        prev_tail = None
        new_head = None
        while pair_start < len(ll_list) - 1:
            if prev_tail is None:
                f_ll = ll_list[pair_start]
                s_ll = ll_list[pair_start + 1]
                s_ll.tail.next = f_ll.head
                new_head = s_ll.head
                prev_tail = f_ll.tail
                pair_start += 2
            else:
                f_ll = ll_list[pair_start]
                s_ll = ll_list[pair_start]
                s_ll.tail.next = f_ll.head
                prev_tail.next = s_ll.head
                prev_tail = f_ll.tail
        return new_head

def print_linked_list(head):
    start = head
    counter = 0
    while start is not None and counter < 10:
        print(start.data)
        start = start.next
        counter += 1


def new_swap(head, n,k):
    if n / k < 2:
        return head
    else:
        counter = 0
        overall_counter = 0
        ll_list = []
        start = head
        start_head = head
        while start is not None:
            counter += 1
            if counter == k:
                counter = 0
                overall_counter += 1
                ll = linked_list(start=start_head, end=start)
                start_head = start.next
                ll_list.append(ll)
                start = start_head
            else:
                start = start.next
            if overall_counter == (n / k):
                if start is not None:
                    if start.next is None:
                        ll = linked_list(start=start_head, end=start)
                        ll_list.append(ll)
                        break

        # print(ll_list)
        # for ll in ll_list:
        #     print ll.head.data, ll.tail.data
        i = 0
        prev_tail = None
        new_head = None
        no_of_pairs = len(ll_list)
        while i<no_of_pairs:
            j = i+1
            if j < no_of_pairs:
                f_ll = ll_list[i]
                s_ll = ll_list[j]

                s_ll.tail.next = f_ll.head

                if prev_tail is None:
                    new_head = s_ll.head
                    prev_tail = f_ll.tail
                    prev_tail.next =None
                else:
                    prev_tail.next = s_ll.head
                    prev_tail = f_ll.tail
                    prev_tail.next = None

                i += 2
            else:
                last_ll = ll_list[i]
                prev_tail.next = last_ll.head
                last_ll.tail.next = None
                break

        return new_head



if __name__ == '__main__':

    n = int(raw_input().strip())
    k = int(raw_input().strip())
    values = map(int, raw_input().strip().split(' '))

    previous_nd = None
    head = None
    for val in values:
        if head is None:
            nd = node(val)
            head = nd
            previous_nd = nd
        else:
            nd = node(val)
            previous_nd.next = nd
            previous_nd = nd
    # print("::")
    # print_linked_list(head)
    head = new_swap(head, n, k)
    print_linked_list(head)


