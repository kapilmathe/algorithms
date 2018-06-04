def nge_array(A, n):
    st = []
    S = [-1]*n
    top = -1
    for i in range(n):
        print(st)
        elem = A[n-i-1]
        while (len(st) > 0 and st[top] < elem):
            st.pop()
            top -=1

        if len(st) <= 0:
            S[n-i-1] = -1
        else:
            S[n-i-1] = st[top]
        st.append(elem)
        top += 1
        # print(S)
    return S


if __name__ == '__main__':
    A = [23,2,54,22,2,1,12]
    n = len(A)
    print(A)
    print(nge_array(A, n))
