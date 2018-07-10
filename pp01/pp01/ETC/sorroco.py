# # Complete the function below.
#
# def solution(array):
#     n = len(array)
#     if n < 3:
#         return array
#     else:
#         start = 0
#         end = 1
#         previous = array[start]
#         result = []
#         for i in range(1, n):
#             print(array[i],previous,i)
#             print(start, end)
#             if (array[i] - previous) == 1:
#                 end = i
#             else:
#                 if end - start >= 2:
#                     result.append("{0}-{1}".format(array[start], array[end]))
#                 else:
#                     print(array[i])
#                     print(array[start:end + 1])
#                     for k in array[start:end + 1]:
#                         result.append("{0}".format(k))
#                 start = i
#                 end = i
#             previous = array[i]
#             print(start, end)
#             print(result)
#         if start == end:
#             return result
#         else:
#             if end - start >=2:
#                 result.append("{0}-{1}".format(array[start], array[end]))
#             else:
#                 for k in array[start:end+1]:
#                     result.append("{0}".format(k))
#             return result
#
#
# array = [-3,-2,-1,5,6,7,9,11,12,13,15,16]
# # array = [12,13,14,15]
# print(solution(array))


# Complete the function below.
# import re
# def find_phone_number(text):
#     pattern1 = re.compile('^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})(?:[0-9])+')
#     pattern2 = re.compile('^[0-9]{3}-[0-9]{3}-[0-9]{4}')
#     pattern3 = re.compile('^(?:[a-z])+([0-9]{3}-[0-9]{3}-[0-9]{4})')
#     if pattern1.match(text):
#         return pattern1.match(text).groups()[0]
#     elif pattern2.match(text):
#         return pattern2.match(text).string
#     elif pattern3.match(text):
#         return pattern3.match(text).groups()[0]
#     else:
#         return None
#
# texts = ["1234567890", "123-456-7890","xxx999-999-9999","(000) 000-0000111"]
# for text in texts:
#     print(find_phone_number(text))

from collections import OrderedDict

def dedup(input_str, chunk_size):
    """
    Args:
        input_str (str): The string on which to deduplicate
        chunk_size(int): Dedup should be done in order of chunk size.

    Returns:
        The deduplicated string
    """
    # Write your code here
    str_od = OrderedDict()
    n = len(input_str)
    chunk_cnt = 0
    print(input_str)
    for i in range(0, n, chunk_size):

        chunk_string = input_str[i:i + chunk_size]
        # print(chunk_string)
        if str_od.get(chunk_string):
            str_od[chunk_string].append(str(chunk_cnt))
        else:
            str_od[chunk_string] = [str(chunk_cnt)]

        chunk_cnt += 1
    return "#".join(["{0},{1}".format(x[0],",".join(x[1])) for x in str_od.items()])


def redup(deduplicated_str, chunk_size):
    """
    Args:
        deduplicated_str(str): The string from the dedup function

    Returns:
        The reconstructed original string
    """
    # Write your code here.
    chunk_strings = deduplicated_str.split("#")
    chunk_list = [x.split(",") for x in chunk_strings]
    total_size = 0
    for cl in chunk_list:
        total_size += len(cl) - 1
    result = [''] * total_size
    print(total_size)
    print(result)
    for ch in chunk_list:
        print(ch)
        for i in range(1, len(ch)):
            print(i)
            result[int(ch[i])] = ch[0]
    return "".join(result)


input_str = "abcdxyzkabcdabcdxyzkabcdabcdxyzkabcd"
chunk_size = 4
out = dedup(input_str, chunk_size)
print(out)
out2 = redup(out,chunk_size)
print(out2)