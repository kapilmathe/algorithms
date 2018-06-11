def chp(A):
    def compare(str1, str2):
        i,j = 0,0
        while (i<len(str1) or j < len(str2)):
            if str1[i] != str2[j]:
                return (str1[i], str2[j])
            else:
                i += 1
                j += 1
        return None

    n = len(A)
    ch_map = {}
    for i in range(n-1):
        str1 = A[i]
        str2 = A[i+1]
        characters = compare(str1, str2)
        ch_map[characters[0]] = 26
        ch_map[characters[1]] = 52

