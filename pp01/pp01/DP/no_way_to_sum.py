def print_matrix(a):
    for l in a:
        print(" ".join([str(x) for x in l]))

combinations = []
def dp_now(s,n,V,comb):
    comb_map = [[]]
    for i in range(V):
        x = []
        for j in range(n):
            x.append(None)
        comb_map.append(x)
    print_matrix(comb_map)

    print("------------")
    for i in range(1,V):
        comb_map[i][0] = 0
    print_matrix(comb_map)
    #
    # for i in range(n):
    #     comb_map[0][i] = 1
    # print("------------")
    # print_matrix(comb_map)



def no_of_way(s, n, V, comb):
    global combinations
    # print(s, n, V, comb)
    if V == 0:
        combinations.append(comb)
        # print(comb)
        return 1
    if V < 0:
        return 0
    if n <= 0 and V>0:
        return 0
    comb2 = list()
    for x in comb:
        comb2.append(x)
    comb2.append(s[n - 1])
    print(n, V)
    return no_of_way(s, n-1, V, comb) + no_of_way(s, n, V-s[n-1], comb2)

if __name__ == '__main__':
    s = [1,2,3]
    n = len(s)
    V = 6
    a = list()
    result = dp_now(s, n, V, a)
    # print(result)
    # print(combinations)

# 33
# 222
# 111111
# 1212
# 312
# 1113
# 11112
#
