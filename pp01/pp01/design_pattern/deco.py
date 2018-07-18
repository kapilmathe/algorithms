# def astrisks(func):
#
#     def inner_ast(*args, **kwargs):
#         val = func(*args)
#         print('*'*val,val,(val+len(str(val))) )
#         return val
#     return inner_ast
#
# @astrisks
# def sum(a, b):
#     return a+b
#
#
# sum(8, 6)


def lsde(strr):
    n = len(strr)
    i = 0
    max_start = 0
    end = 0
    curr = 0
    char_dict = {}
    while i < n:
        if char_dict.get(strr[i]):
            if ((i-1) - curr) >= (end - max_start):
                max_start = curr
                end = i-1
                curr = i
            i += 1
        else:
            char_dict[strr[i]] = True
            i += 1
    if ((i-1)-curr) > (max_start-end):
        max_start = curr
        end = i-1
    print(max_start, end)
    return strr[max_start:end+1]

# strr = 'defaasdf'
strr = 'aaaaaaaa'
print(len(strr))
print(lsde(strr))