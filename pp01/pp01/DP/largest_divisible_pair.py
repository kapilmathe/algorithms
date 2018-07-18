# https://www.geeksforgeeks.org/largest-divisible-pairs-subset/
def ldp(a, n):
    a.sort()
    if n < 0:
        return 0
    if n == 0:
        return 1
    S = [1]*n
    max_so_far = -1
    for i in range(n):
        curr = a[i]
        for j in range(i+1, n):
            if a[j]%curr == 0:
                curr = a[j]
                S[i] += 1
                if max_so_far <S[i]:
                    max_so_far = S[i]
    return max_so_far



a = [10, 3, 5, 5, 3, 15, 20]
# a= [18, 1, 3, 6, 13, 17]
n = len(a)
print(ldp(a,n))