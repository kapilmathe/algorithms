def print_matrix(S):
    for x in S:
        print(x)

def subarray_sum(A, SAS):
    n = len(A)
    S = []
    for i in range(n):
        S.append([0]*n)
    for i in range(n):
        for j in range(i,n):
            if i==j:
                S[i][j] = A[i]
            else:
                S[i][j] = S[i][j-1] + A[j]
            if S[i][j] == SAS:
                return "{0} {1}".format(i+1,j+1)
    return "-1"


T = int(input().strip())
result = []
for i in range(T):
    N, S = [int(x) for x in input().strip().split(' ')]
    A = [int(x) for x in input().strip().split(' ')]
    result.append(subarray_sum(A, S))

for res in result:
    print(res)
# A = [1,2,3,7,5]
# SAS = 12
# print(subarray_sum(A,SAS))