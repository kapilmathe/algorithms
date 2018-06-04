INT_MIN = -22133123123323
INT_MAX = 22133123123323


def min_jump_non_dp(arr, i, N):
    print("""({0}, {1})""".format(i, N))
    if (arr[i] == 0):
        return INT_MAX
    if arr[i] >= (N - i):
        return 1
    else:
        min = INT_MAX
        for j in range(arr[i]):
            val = 1 + min_jump_non_dp(arr, i + j + 1, N)
            if min > val:
                min = val
        return min


def dp_min_jump(arr, i, N):
    cach = [None]*N
    def min_jump(arr, i, N):
        if cach[i]:
            return cach[i]
        if (arr[i] == 0):
            cach[i] =  INT_MAX
            return INT_MAX
        if arr[i] >= (N-i):
            cach[i] = 1
            return 1
        else:
            min = INT_MAX
            print("""({0}, {1}) = {2}""".format(i,N,cach[i]))
            for j in range(arr[i]):
                cach[i+j+1] = min_jump(arr, i+j+1, N)
                if min > cach[i+j+1]:
                    min = cach[i+j+1]
            cach[i] =  min + 1
            return cach[i]
    val = min_jump(arr, i, N)
    return val


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
# arr = [1, 3, 6, 1, 0, 9]
N = len(arr)
# print(min_jump_non_dp(arr, 0, N))
# minjump = dp_min_jump()
print(min_jump_non_dp(arr, 0, N))