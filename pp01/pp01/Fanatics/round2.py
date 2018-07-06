def shift_zero(a):
    n = len(a)
    i = 0
    j = i + 1
    while i < n and j < n:
        if a[i] == 0:
            while j < n and a[j] > 0:
                a[i] = a[j]
                j += 1
                i += 1
            a[i] = 0
            j += 1
        else:
            i += 1
            j += 1
    while i < j and i<n:
        print(i)
        a[i] = 0
        i += 1
    return arr


arr = [1, 0, 4, 7, 2, 0, 0, 5, 1, 4]

print(shift_zero(arr))
