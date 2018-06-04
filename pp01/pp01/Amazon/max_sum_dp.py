def dp_max_sum(A, n):
    ms = {0:0}
    def max_s(A,n):

        if ms.get(n):
            return ms[n]
        else:
            if n<=2:
                ms[n] = max(A)
            elif n==3:
                ms[n] = A[0]+A[2]
            else:
                print(A, "--", n)
                ms[n] = max(max_s(A[:n-1], n-1), A[n-1]+ max_s(A[:n-2], n-2))
            return ms[n]
    val = max_s(A,n)
    return val


def max_sum(A, n):

    if n == 0:
        return 0
    elif n <= 2:
        return max(A)
    elif n == 3:
        return A[0]+A[2]
    else:
        print(A, "--", n)
        return max(max_sum(A[:n-1], n-1), A[n-1]+ max_sum(A[:n-2], n-2))

if __name__ == '__main__':
    A = [5, 5, 10, 100, 10, 5,23,12,54,12,43,23]
    # A = [3,2,7,10]
    # A = [3,2,5,10,7]
    n = len(A)
    print(dp_max_sum(A,n))
    print('---------')
    print(max_sum(A,n))