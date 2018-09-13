# include <iostream>
# include <string>
# include <vector>


# Print all the k combinations of the n numbers
# [1, 2, 3, 4 ,5, 6, 7, 8]

# k = 2
# 1,2 1,3 2,3

# using namespace std;

# int main() {
#     /* Enter your code here. Read input from STDIN. Print output to STDOUT */
#     return 0;
# }

def get_combination(combination, number_set, length, position):
    if len(combination) == length:
        print(combination)
        return True
    for x in number_set:
        number_set = number_set - set((x,))
        combination2 = combination + (x,)
        get_combination(combination2, number_set, length)


def print_all_combination(arr, k):
    combination = tuple()
    number_set = set(arr)
    get_combination(combination, number_set, k)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4
print_all_combination(arr, k)