def number_needed(a, b):
    a_dict = {}
    b_dict = {}

    for x in list('abcdefghijklmnopqrstuvwxyz'):
        a_dict[x] = 0
        b_dict[x] = 0

    for x in list(a):
        a_dict[x] += 1

    for x in list(b):
        b_dict[x] += 1
    letter_to_del = 0
    for key, val in a_dict.iteritems():
        letter_to_del += abs(val - b_dict[key])
    return letter_to_del


a = raw_input().strip()
b = raw_input().strip()

print(number_needed(a, b))