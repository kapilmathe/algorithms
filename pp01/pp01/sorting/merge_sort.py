def merge(f,s):
    i, j= 0, 0
    m, n = len(f), len(s)
    result = []
    while (i < m or j < n):
        if i >= m:
            while j < n:
                result.append(s[j])
                j += 1
            return result
        elif j >= n:
            while i < m:
                result.append(f[i])
                i += 1
            return result
        if f[i] < s[j]:
            result.append(f[i])
            i += 1
        else:
            result.append(s[j])
            j += 1
    return result

def merg_sort(A):
    n = len(A)
    if n == 1:
        return A
    else:
        mid = n/2
        result = merge(merg_sort(A[0:mid]), merg_sort(A[mid:n]))
        return result

A = [5,2,1,7,9,3,5,4]
print(merg_sort(A))