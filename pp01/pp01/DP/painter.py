def get_painter_time(A, n, k):
    s = 0
    for x in A:
        s += x
    if k == 1:
        return s
    else:
        print("s={0}".format(s))
        lo = s/k
        p_cnt = k
        p_sum = 0
        max_time = 0
        for i in range(n):
            p_sum += A[i]
            print("p_sum={0}".format(p_sum))
            if p_sum >= lo:
                p_cnt -= 1
                if max_time < p_sum:
                    max_time = p_sum
                p_sum = 0
        print(p_cnt)
        return max_time

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(A)
    k = 3
    print(get_painter_time(A,n,k))