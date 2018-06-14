def finding_numbers(A):
    n = len(A)
    num_dict = {}
    for x in A:
        if num_dict.get(x):
            del num_dict[x]
        else:
            num_dict[x] = 1

    return list(num_dict.keys())


T = int(input().strip())
result = []
for i in range(T):
    n = int(input().strip())
    A = [int(x) for x in input().strip().split(' ')]
    # print(A)
# A = [1, 2, 3, 2, 1, 4]
    r = finding_numbers(A)
    result.append(r)
for rr in result:
    rr.sort()
    print("{0} {1}".format(rr[0],rr[1]))