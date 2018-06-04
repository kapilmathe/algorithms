# def f_o(S, t, c, L):

def fibbo(n):
    a = [0,1]
    for i in range(2,12):
        a.append(a[i-1]+a[i-2])
    return a


def knapsack(W,V,N,M,x):
    print(N, M, x)
    W = [x*val for val in W]
    V = [x*val for val in V]
    if N == 0 or M == 0:
        return 0
    if(W[N-1] > M):
        return knapsack(W,V,N-1,M,x)
    else:
        return max(
            V[N-1]+ knapsack(
                W,
                V,
                N-1,
                M-W[N-1],
                x
            ),
            knapsack(
                W,
                V,
                N-1,
                M,
                x
            )

        )

T = int(raw_input().strip())
X = fibbo(100)
print(X[1:])
# exit()
for i in range(T):
    N, M = map(int, raw_input().strip().split(' '))
    W = map(int, raw_input().strip().split(' '))
    V = map(int, raw_input().strip().split(' '))
    result= []
    for x in X[1:]:
        result.append(knapsack(W,V,N,M,x))

print((result))
