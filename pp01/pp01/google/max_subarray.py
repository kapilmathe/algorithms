INT_MIN = -999999999999
INT_MAX = 999999999999


def find_max_cross_subarray(A, low, mid, high):
    left_sum = INT_MIN
    left_low = None
    curr_sum = 0
    for i in range(mid, low-1, -1):
        curr_sum += A[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
            left_low = i

    right_sum = INT_MIN
    right_high = None
    curr_sum = 0
    for i in range(mid+1, high):
        curr_sum += A[i]
        if curr_sum > right_sum:
            right_sum = curr_sum
            right_high = i

    return (left_low, right_high, left_sum+right_sum)


def max_sub_array(A, low, high):
    # print(low, high)
    if high == low:
        return (low, high, A[low])
    else:
        mid = int((low+high)/2)
        left_low, left_high, left_sum = max_sub_array(A, low, mid)
        right_low, right_high, right_sum = max_sub_array(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_cross_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

A= [-2,-3, 4, -1, -2, 1, 5, -3]
print(max_sub_array(A, 0, len(A)-1))