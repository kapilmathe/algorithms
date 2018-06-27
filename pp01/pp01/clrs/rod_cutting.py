INT_MIN = -1

def rod_cut(a, n):
    if n == 0:
        return 0
    else:
        q = INT_MIN
        for i in range(1,n+1):
            q = max(q, a[i]+rod_cut(a, n-i))
        return q

def rod_cut_tb(a,n):
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
                x = a[i]+ rod_cut_top_bottom(a, n-i)
                q = max(q, x)
            s[n-1] = q
            return q
    result = rod_cut_top_bottom(a, n)
    return result

def rod_cut_bt(a,n):
    s = [-1]*(n+1)
    s[0] = 0
    for i in range(1,n+1):
        q = INT_MIN
        for j in range(1,i+1):
            q = max(q, a[j]+s[i-j])
        s[i] = q

    return s[n]

a = [0,1,5,8,9,10,17,17,20,24,30,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
n = 50
print(rod_cut_tb(a, n))
print(rod_cut_bt(a, n))