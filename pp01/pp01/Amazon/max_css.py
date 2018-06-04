result = []
def print_matrix(a):
    for l in a:
        print(" ".join([str(x) for x in l]))

def dp_max_css(str1, str2, n, m):
    max_css_map = [[-1]*(m+1)]*(n+1)
    print_matrix(max_css_map)
    for j in range(m+1):
        max_css_map[0][j] = 0

    print_matrix(max_css_map)
    for i in range(n+1):
        max_css_map[i][0] = 0
    print_matrix(max_css_map)
    print("------------")
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                max_css_map[i][j] = 1+max_css_map[i-1][j-1]
            else:
                max_css_map[i][j] = max(
                    max_css_map[i][j-1],
                    max_css_map[i-1][j]
                )
    print_matrix(max_css_map)
    return max_css_map[n][m]


def dp_max_css2(str1, str2, n, m):
    max_css_map = [[-1] * (m + 1)] * (n + 1)
    def max_cs(str1, str2, n, m):
        if m == 0 or n == 0:
            return 0
        if max_css_map[n][m] >= 0:
            return max_css_map[n][m]
        else:
            print("(n,m)=({0},{1})".format(n, m))
            if str1[n-1] == str2[m-1]:

                max_css_map[n][m] = 1+max_cs(str1, str2, n-1, m-1)
                return max_css_map[n][m]
            else:
                max_css_map[n][m] = max(
                    max_cs(str1, str2, n, m-1),
                    max_cs(str1, str2, n-1, m)
                )
                return max_css_map[n][m]
    result = max_cs(str1, str2, n, m)
    return result


def max_css(str1, str2, n, m):
    if m == 0 or n == 0:
        return 0
    else:
        print("(n,m)=({0},{1})".format(n,m))
        if str1[n-1] == str2[m-1]:
            return 1+max_css(str1, str2, n-1, m-1)
        else:
            return max(
                max_css(str1, str2, n, m-1),
                max_css(str1, str2, n-1, m)
            )


if __name__ == '__main__':
    str2 = 'saturday'
    str1 = 'sunday'
    n = len(str1)
    m = len(str2)
    # max_css_len = max_css(str1, str2, n, m)
    # print(max_css_len)
    print("----")
    print(dp_max_css(str1, str2, n, m))
    # print(dp_max_css2(str1, str2, n, m))
    # ans = abs(max(m,n)-max_css_len)
    # print("--")
    # print(ans)
    # print(set(result))
