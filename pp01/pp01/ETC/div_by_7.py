'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here

def sub_list(A, B):
    n1, n3 = len(A), len(B)
    if n1 < n3:
        return None
    B = ['0']*(n1-n3)+B
    n2 = len(B)
    result = []
    po = 0
    for i in range(1,n1+1):
        # print("i={0}".format(i))
        # print("po={0}".format(po))
        B1 = int(B[n2 - i])
        A1 = int(A[n1 - i])
        # print("A1={0}, B1={1}".format(A1,B1))
        sub = A1 - B1 + po
        if sub < 0:
            val = 10 + sub
            po = -1
        else:
            val = sub
            po = 0
        # print(po,i)
        result.append(str(val))
    # print("result={0}".format(res))
    return list(result)


def is_div_7(N, L, R):
    # print (L,R)
    start = N[L - 1: R]
    start_len = len(start)
    # l_digit = int(N[R - 1])
    while start_len > 100:
        l_digit = int(start[start_len - 1])
        B = list(str(2 * l_digit))
        start = start[:start_len-1]
        # print(start)
        # print(B)
        print("starting start={0}".format(start))
        start = sub_list(A=start, B=B)
        start.reverse()
        print("ending start={0}".format(start))
        start_len = len(start)

    num = int("".join(start))
    if num % 7 == 0:
        return 'YES'
    else:
        return 'NO'


n_str = raw_input().strip()
q = long(raw_input().strip())
a = list(n_str)
for j in range(q):
    L, R = raw_input().strip().split(' ')
    res = is_div_7(a, int(L), int(R))
    print(res)
