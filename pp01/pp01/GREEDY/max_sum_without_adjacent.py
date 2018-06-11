def mswa_dp(A, n):
    cache = [None]*(n+1)
    def mswa(A, n):
        if n <= 0:
            return 0
        if n == 1:
            return A[0]
        if cache[n]:
            return cache[n]
        else:
            cache[n] = max(mswa(A, n-1), A[n-1]+mswa(A, n-2))
        return cache[n]
    result = mswa(A, n)
    return result


A = [3,2,7,10]
# A = [5,5,10,100,10,5]
n = len(A)
print(mswa_dp(A, n))