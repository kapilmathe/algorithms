def perform_left(start, final):
    start = (start[0]+start[1], start[1])
    if start == final:
        return start
    elif start[0] > final[0] or start[1] > final[1]:
        return tuple()
    else:
        return start

def perform_right(start, final):
    start = (start[0], start[1]+start[0])
    if start == final:
        return start
    elif start[0] > final[0] or start[1] > final[1]:
        return tuple()
    else:
        return start


def is_possible(a, b, c, d):
    # print(a, b, c, d)
    start = (a, b)
    final = (c, d)
    if start == final:
        return 'Yes'
    else:
        left = perform_left(start, final)
        right = perform_right(start, final)
        if left == final or right == final:
            return 'Yes'
        if len(left):
            return is_possible(left[0], left[1], c, d)
        if len(right):
            return is_possible(right[0], right[1], c, d)
        return 'No'


if __name__ == '__main__':
    test_cases = [
        (1, 4, 5, 9),
        (2, 3, 5, 6)
    ]
    for test in test_cases:
        print(is_possible(*test))

