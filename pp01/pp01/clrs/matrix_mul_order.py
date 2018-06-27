def is_compatible(x, y):
    if x[1] == y[0]:
        return True
    else:
        return False


def no_of_multiplication(x, y):
    return x[0]*x[1]*y[1]

def get_size(x):
    return x[0]*x[1]


def min_mat_mul(mat_order):
    n = len(mat_order)
    if n < 2:
        return None
    mat_size = []
    mat_list = [(mat_order[0], mat_order[1])]
    mat_size.append(mat_order[0]*mat_order[1])
    min_size_index = 0
    min_size_so_far = mat_size[min_size_index]
    for i in range(1,n-1):
        mat_list.append((mat_order[i],mat_order[i+1]))
        mat_size.append(mat_order[i]*mat_order[i+1])
        if mat_size[i] < min_size_so_far:
            min_size_so_far = mat_size[i]
            min_size_index = i

    # current_left = mat_list[0]
    # print(mat_list)
    multiplication_count = 0
    left = min_size_index-1
    right =min_size_index+1
    curr_l_mul = None
    curr_r_mul = None
    curr_matrix = mat_list[min_size_index]
    while left >= 0 or right < n-1:
        # print(left, min_size_index, right ,n-1)
        if left >= 0:
            curr_l_mul = no_of_multiplication(mat_list[left], curr_matrix)
        if right < n-1:
            curr_r_mul = no_of_multiplication(curr_matrix, mat_list[right])

        if curr_r_mul is not None and curr_l_mul is not None:
            # print("case1")
            if get_size(mat_list[right]) > get_size(mat_list[left]):
                multiplication_count += curr_r_mul
                curr_matrix = (curr_matrix[0], mat_list[right][1])
                right += 1
            else:
                multiplication_count += curr_l_mul
                curr_matrix = (mat_list[left][0], curr_matrix[1])
                left -= 1
            # print(multiplication_count, curr_matrix)

            curr_l_mul = None
            curr_r_mul = None
        elif curr_r_mul is None and curr_l_mul is not None:
            # print("case2")
            multiplication_count += curr_l_mul
            curr_matrix = (mat_list[left][0], curr_matrix[1])
            # print(multiplication_count, curr_matrix)
            left -= 1
            curr_l_mul = None
        elif curr_r_mul is not None and curr_l_mul is None:
            # print("case3")
            multiplication_count += curr_r_mul
            curr_matrix = (curr_matrix[0], mat_list[right][1])
            right += 1
            curr_r_mul = None
        else:
            # print("case4")
            return multiplication_count
    return multiplication_count
    # for i in range(1,n-1):
    #         print(i)
    #         current_right = mat_list[i]
    #         if is_compatible(current_left, current_right):
    #             multiplication_count += no_of_multiplication(current_left, current_right)
    #             current_left = (current_left[0], current_right[1])
    #

    # print(mat_size)
    # return multiplication_count

# l = [40, 20, 30, 10, 30]
# l = [10, 20, 30, 40, 30]
T = int(input())
result = []
for i in range(T):
    N = int(input())
    l = [int(x) for x in input().split(' ')]
    result.append(min_mat_mul(l))

for res in result:
    print(res)