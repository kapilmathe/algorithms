INT_MIN = -1

def rod_cut(a, n, c):
    if n == 0:
        return 0
    else:
        q = INT_MIN
        for i in range(1,n+1):
            cc = c if n-i else 0
            q = max(q, a[i-1]+rod_cut(a, n-i, c) - cc)
        return q

def rod_cut_tb(a,n,c):
    s = [-1]*(n+1)
    def rod_cut_top_bottom(a, n):
        if n == 0:
            return 0
        if s[n-1] >= 0:
            return s[n-1]
        else:
            q = INT_MIN
            # print(n)
            for i in range(1,n+1):
                cc = c if n-i else 0
                x = a[i-1]+ rod_cut_top_bottom(a, n-i) - cc
                q = max(q, x)
            s[n-1] = q
            return q
    result = rod_cut_top_bottom(a, n)
    return result

def rod_cut_bt(a,n,c):
    s = [-1]*(n+1)
    r = []
    s[0] = 0
    for i in range(1,n+1):
        q = INT_MIN
        index = None
        for j in range(1,i+1):
            cc = c if i-j else 0
            if a[j-1]+s[i-j] -cc > q:
                index = j
                q = a[j-1]+s[i-j] - cc
            # q = max(q, a[j]+s[i-j])
        r.append(index)
        s[i] = q
    print(r)
    return s[n]

a = [1,5,8,9,10,17,17,20,24,30,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
n = 11
c = 4
print(rod_cut(a, n, c))
print(rod_cut_tb(a, n, c))
print(rod_cut_bt(a, n, c))