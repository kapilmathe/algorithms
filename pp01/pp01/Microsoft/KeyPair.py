# https://practice.geeksforgeeks.org/problems/key-pair/0
def key_pair(a, n, x):
    a.sort()
    i = 0
    j = n-1
    while i < j:
        if a[i]+a[j] > x:
            j -= 1
        elif a[i]+a[j] < x:
            i += 1
        else:
            return 'Yes'
    return 'No'


t = int(input().strip())
for i in range(t):
    n, x = (int(x) for x in input().strip().split(' '))
    arr = [int(x) for x in input().strip().split(' ')]
    print(key_pair(arr, n, x))

