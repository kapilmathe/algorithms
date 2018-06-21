# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0

def max_subarray(A):
    start = None
    end = None
    max_ending_here = max_so_far = A[0]
    for x in range(1, len(A)):
        max_ending_here += A[x]
        if max_ending_here < 0:
            max_ending_here = 0
            start = x+1
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = x
        max_so_far = max(max_so_far, max_ending_here)
    return start-1, end, max_so_far

def max_stop(A):
    n = len(A)
    last_price = A[0]
    price_change = []
    for x in A:
        price_change.append(x - last_price)
        last_price = x

    print(price_change)

    # kadanes theorem
    # return  max_subarray(price_change)
    max_so_far = max_current = 0
    max_so_far_start = 0
    max_so_far_end = 0
    range_set = []
    for i in range(n):
        max_current += price_change[i]
        if max_current > max_so_far:
            max_so_far = max_current
            max_so_far_end = i
        if max_current < 0:
            max_current = 0
            range_set.append((max_so_far_start, i-1))
            max_so_far_start = i+1
    range_set.append((max_so_far_start-1, max_so_far_end))
    return range_set


# A = [100, 180, 260, 310, 40, 535, 695]
A = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
print(max_stop(A))
