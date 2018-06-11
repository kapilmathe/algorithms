def four_elem(A, n, k, X, result = None):
    print("n={0}/k={1}/X={2}".format(n,k,X))
    if X <0 :
        return []
    if result is None:
        result = []
    if X == 0 and k == 0:
        return []
    if n < k:
        return None
    if n == k:
        if sum(A) == X:
            return A
        else:
            return None
    # if A[n-1] > X:
    #     # exclude last element
    #     return four_elem(A, n-1, k, X, result)
    r1 = four_elem(A, n-1, k, X, result)
    if r1:
        r1.append(A[n-1])
        if len(r1) == k:
            return r1
    result.append(A[n-1])
    r2 = four_elem(A, n - 1, k - 1, X - A[n - 1], result)
    if r2 and len(r2) == 4:
        return r2
    return None

A = [1,3,23,2,4,6]
n = len(A)
k = 4
X= 10
r = four_elem(A,n,k,X)
print(r)