# https://www.geeksforgeeks.org/sequences-given-length-every-element-equal-twice-previous/
def print_matrix(a):
    for l in a:
        print(" ".join([str(x) for x in l]))


def equal_or_twice(n,m):
    if n == 0:
        return 1
    T = [[0]*(m+1) for _  in range(n+1)]
    T[0][0] = 1
    for i in range(1,n+1):
        T[i][0] = 0

    for i in range(1, m+1):
        T[0][i] = 1

    # print_matrix(T)

    for i in range(1,n+1):
        for j in range(1,m+1):
            T[i][j] = 0
            k = j
            T[i][j] = T[i][j-1] + T[i-1][j//2]
            # while k > 0:
            #     T[i][j] += T[i-1][k//2]
            #     k -= 1

    # print("####################")
    print_matrix(T)
    return T[n][m]


inps = [(4, 10), (2,5)]
no_i = int(input().strip())
for _ in range(no_i):
# for inp in inps:
    m, n = [int(x)  for x in input().strip().split(' ')]
    # n = int(input().strip())
    res = equal_or_twice(n,m)
    print("{0}".format(res))
    # print("#################### END ")
