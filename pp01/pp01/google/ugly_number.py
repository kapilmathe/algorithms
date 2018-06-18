def get_nth_ugly_number(n):
    ugly_number = [0] * n
    ugly_number[0] = 1
    i2 = i3 = i5 = 0
    next_2_sequence_number = 1*2
    next_3_sequence_number = 1*3
    next_5_sequence_number = 1*5
    i = 1
    for i in range(1,n):
        next_ugly = min(next_2_sequence_number, next_3_sequence_number, next_5_sequence_number)
        ugly_number[i] = next_ugly

        if next_ugly == next_2_sequence_number:
            i2 += 1
            next_2_sequence_number = ugly_number[i2] *2
        if next_ugly == next_3_sequence_number:
            i3 += 1
            next_3_sequence_number = ugly_number[i3] *3
        if next_ugly == next_5_sequence_number:
            i5 += 1
            next_5_sequence_number = ugly_number[i5] *5
    return ugly_number[n-1]


n = 150
print(get_nth_ugly_number(n))