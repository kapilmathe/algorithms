def my_sort(a):
    num_dict = {0:0, 1:0, 2:0}
    n = len(a)
    l = 0
    r = n-1
    c1 = 0
    c2 = n-1
    result = [None]*n
    for i in range(n):
        if a[i] == 1:
            result[c1] = 1
            c1 += 1
        elif a[i] == 2:
            result[c2] = 2
            c2 -= 1
    return result

# I/O - reading 2MB takes 2 seconds: 10 MB - 10 Seconds
# single thread = 10 seconds + 2 seconds = 12
#
# multi threads = 5
# thread 1 = 2 MB = 2, 2
# thread1-1-thread2-1


    # while c1 <= c2:
    #
    #     if a[c2]  == 1:
    #         a[c1], a[c2] = a[c2], a[c1]
    #
    #     if a[c1] == 2:
    #         a[c2], a[c1] = a[c1], a[c2]
    #     c2 -= 1
    #     c1 += 1
    # return a
# [2,1,2,1,1,1]
#     while l<=r: # n/2
#         num_dict[a[l]] += 1
#         num_dict[a[r]] += 1
#         l += 1
#         r -= 1
#
#
#     for i in range(n):
#         if num_dict[0]:
#             a[i] = 0
#             num_dict[0] -= 1
#         elif num_dict[1]:
#             a[i] = 1
#             num_dict[1] -= 1
#         else:
#             a[i] = 2
#             num_dict[2] -= 1
#     return a

def sort_deco(fn):
    def inner(*args):
        print(args)
        a = args[0]
        a = my_sort(a)
        return fn(a)
    return inner

@sort_deco
def test(A):
    print("kapil")
    print(A)

A = [1,2,1,2,1]
test(A)
# print(A)
# test(A)