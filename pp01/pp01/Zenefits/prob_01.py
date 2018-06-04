def get_l(x):
    val = ord(x)
    new_val = val -1
    if new_val < 97:
        return chr(122)
    else:
        return chr(new_val)


def get_r(x):
    r = (97, 122)
    val = ord(x)
    new_val = val +1
    if new_val > 122:
        return chr(97)
    else:
        return chr(new_val)

def process_subs(s, i,j,action):
    if action == 'L':
        for cur in range(i,j+1):
            s[cur] = get_l(s[cur])
    else:
        for cur in range(i,j+1):
            s[cur] = get_r(s[cur])
    return s


if __name__ == '__main__':
    s = list(raw_input().strip())
    n = int(raw_input().strip())
    for i in range(n):
        i, j , action = raw_input().rstrip().split(' ')
        i = int(i)
        j = int(j)
        s = process_subs(s, i, j, action)
    print("".join(s))
