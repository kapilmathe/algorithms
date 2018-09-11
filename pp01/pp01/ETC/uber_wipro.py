# Enter your code here. Read input from STDIN. Print output to STDOUT
# abcabcbb Longest substring with non repeating characters
# input = ABDEFGABEF
# output DEFGAB or BDEFGA or ABDEFG
def l_sub(s):
    j = 0
    ch_map = {}
    max_so_far = list()
    ml = 0
    for i in range(len(s)):
        x = s[i]
        # print(j,i)
        if ch_map.get(x):
            if (i - j) > ml:
                max_so_far = list()
                max_so_far.append(s[j:i - 1])
                ml = (i - j)
            elif (i - j) == ml:
                max_so_far.append(s[j:i - 1])

            j = ch_map[x] + 1
            ch_map[x] = i


        else:
            ch_map[x] = i

        if (i - j + 1) > ml:
            max_so_far = list()
            max_so_far.append(s[j:i + 1])
            ml = (i - j + 1)
        elif (i - j + 1) == ml:
            max_so_far.append(s[j:i + 1])
    return max_so_far


inp = [
    'ABDEFGABEF'
]# Enter your code here. Read input from STDIN. Print output to STDOUT
# abcabcbb Longest substring with non repeating characters
#input = ABDEFGABEF
#output DEFGAB or BDEFGA or ABDEFG
def l_sub(s):
    j = 0
    ch_map = {}
    max_so_far = list()
    ml = 0
    for i in range(len(s)):
        x = s[i]
        # print(x,i)
        # print(j,i)
        if ch_map.get(x) is not None:
            # print(ch_map)
            # if (i-j) > ml:
            #     print(s[j:i])
            #     max_so_far = list()
            #     max_so_far.append(s[j:i])
            #     ml = (i-j)
            # elif (i-j) == ml:
            #     print(s[j:i-1])
            #     max_so_far.append(s[j:i])

            j = ch_map[x]+1
            ch_map[x] = i


        else:
            ch_map[x] = i

        if (i-j+1) > ml:
            # print("--2",s[j:i+1])
            max_so_far = list()
            max_so_far.append(s[j:i+1])
            ml = (i-j+1)
            print("--2", s[j:i + 1], ml)
        elif (i-j+1) == ml:
            print("--2",s[j:i-1], ml)
            max_so_far.append(s[j:i+1])
    return max_so_far



inp = [
    'ABDEFGABEF'
    ]

for s in inp:
    print(l_sub(s))

