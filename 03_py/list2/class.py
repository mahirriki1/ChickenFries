# TODO:
# - add test cases
# - add comments

def count_evens(nums):
    count = 0 
    for num in nums:
        if num % 2 == 0: # if num is divisble by 2
            count += 1
    return count

def big_diff(nums):
    small = nums[0]
    big = nums[0]
    for num in nums:
        small = min(small, num)
        big = max(big, num)
    return big - small

def centered_average(nums):
    small = nums[0]
    big = nums[0]
    for num in nums:
        small = min(small, num)
        big = max(big, num)
    sum = 0
    for num in nums:
        sum += num
    return (sum - (small + big)) / (len(nums) - 2)

def sum13(nums):
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i != len(nums) - 1:
                nums[i + 1] = 0
    sum = 0
    for num in nums:
        sum += num
    return sum

def sum67(nums):
    # work on later
    return 0