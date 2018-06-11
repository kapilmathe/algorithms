def no_of_zeros(n):
    factor_map = {2: 0, 5: 0}
    for x in range(n, 0, -1):
        i = x
        j = x
        while i%2 == 0:
            factor_map[2] += 1
            i = i/2
        while j%5 == 0:
            factor_map[5] += 1
            j = j/5
    print(factor_map)
    return min(factor_map.values())


n = 10
print(no_of_zeros(n))