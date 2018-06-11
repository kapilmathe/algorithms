def toh(h, A, B, C):
    if h == 1:
        print("move -{0}- disk from A to C".format(h))
    else:
        toh(h-1, A, C, B)
        print("move -{0}- disk from {1} to {2}".format(h, A, C))
        toh(h-1, B, C, A)


toh(4, 'A', 'B', 'C')