def maximum_index(A):
    n = len(A)
    max_diff = 0
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if A[j]>= A[i]:
                # print(A[j], A[i])
                max_diff = max(max_diff, (j-i))
    return max_diff


def max_diff2(A):
    n = len(A)
    l_min  = [0]*n
    r_max = [0]*n
    l_min[0] = A[0]
    for i in range(1,n):
        l_min[i] = min(l_min[i-1], A[i])

    r_max[n-1] = A[n-1]
    for j in range(n-2,-1, -1):
        r_max[j] = max(A[j], r_max[j+1])

    i = 0
    j = 0
    max_diff = -1
    print(A)
    print(l_min)
    print(r_max)
    while (i<n and j<n):
        if (l_min[i] < r_max[j]):
            max_diff = max(max_diff, j-i)
            j += 1
        else:
            i += 1
    return max_diff

A = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
# print(maximum_index(A))
print(max_diff2(A))