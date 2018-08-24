def sh(nums):
    first = None
    second = None
    for num in nums:
        if first is None or first < num:
            # print(num)
            second = first
            first = num
        elif second is None or (second < num and num != first):
            second = num
    return second


nums = [2, 3, 6, 6, 5]
print(sh(nums))
