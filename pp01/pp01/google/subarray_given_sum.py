# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
def sags(A, n, S):
    if S > 0 and n==0:
        return -1
    TS = sum(A)
    if S > TS:
        return -1
    if S == TS:
        return (0,n-1)
    cumm_sum = {}
    cumm_sum_index = {}
    curr_sum = 0
    for i in range(n):
        curr_sum += A[i]
        cumm_sum[i] = (curr_sum)
        cumm_sum_index[curr_sum] = i
        if curr_sum == S:
            return (0,i)

    possible_sa = []
    for i in range(n):
        if cumm_sum[i] > S:
            possible_sa.append((i,cumm_sum[i] - S))
    # print(possible_sa)
    for idx in range(len(possible_sa)):
        end, val = possible_sa[idx]
        if cumm_sum_index.__contains__(val):
            return (cumm_sum_index[val]+1,end)

    return -1


A = [1,2,3,4,5,6,7,8,9,10]
S = 15
print(sags(A, len(A), S))