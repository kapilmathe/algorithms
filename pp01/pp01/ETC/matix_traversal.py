def spiral_matrix(A, m, n):
    tr = 0
    rc = n-1
    br = m-1
    lc = 0
    direction = 0
    data = []
    while (tr <= br and lc <= rc):
        if direction == 0:
            print(lc,rc+1)
            for i in range(lc,rc+1):
                data.append(A[tr][i])
            tr += 1
            direction = 1
        # print(data)
        elif direction == 1:
            print(tr, br+1)
            for i in range(tr, br+1):
                data.append(A[i][rc])
            rc -= 1
            direction = 2
        elif direction == 2:
            print(rc, lc-1)
            for i in range(rc, lc-1, -1):
                data.append(A[br][i])
            br -= 1
            direction = 3
        elif direction == 3:
            print(br, tr-1)
            for i in range(br, tr-1, -1):
                data.append(A[i][lc])
            lc += 1
            direction = 0
    print(data)


if __name__ == '__main__':
    A = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21, 22,23,24,25],
        # [13,14,15,16]
    ]
    n = len(A[0])
    m = len(A)
    # print(m,n)
    spiral_matrix(A, m, n)