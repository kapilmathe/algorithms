# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input().strip()


def str_cmp(a, b):
    val1, val2 = 0, 0
    if a.isdigit():
        if int(a) % 2:
            val1 = 100 + int(a)
        else:
            val1 = 110 + int(a)
    else:
        if ord(a) >= 97:
            val1 = ord(a) - 60
        else:
            val1 = ord(a)
    if b.isdigit():
        if int(b) % 2:
            val2 = 100 + int(b)
        else:
            val2 = 110 + int(b)
    else:
        if ord(b) >= 97:
            val2 = ord(b) - 60
        else:
            val2 = ord(b)

    return val1 - val2

print ("".join(sorted(S, cmp=str_cmp)))