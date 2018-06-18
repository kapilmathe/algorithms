# def bst_search(A, low, high, val):
#     # print(low,high )
#     if low > high:
#         return None
#     if low == high:
#         if val == A[low]:
#             return low
#         else:
#             return None
#
#     mid = int((low+high)/2)
#     if A[mid] == val:
#         return mid
#     elif A[mid] > val:
#         return bst_search(A, low, mid, val)
#     else:
#         return bst_search(A, mid+1, high, val)



def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()
    print(arr)
    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):

            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True


            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    if (found == False):
        print(" No Triplet Found")


# A = [-3,-1,0,2,1]
A = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
n = len(A)
# print(n)
findTriplets(A, n)