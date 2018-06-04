def ransom_note(magazine, ransom):
    # print(magazine)
    # print(ransom)
    mag_hash = {}
    ran_hash = {}
    for x in magazine:
        if mag_hash.get(x):
            mag_hash[x] += 1
        else:
            mag_hash[x] = 1
    # print(mag_hash)
    for y in ransom:
        # print y
        if mag_hash.get(y):
            mag_hash[y] = mag_hash[y] - 1
        else:
            return 'No'
    return 'Yes'


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
print answer

