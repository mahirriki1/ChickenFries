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

# work on this later
def sum13(nums):
    if len(nums) == 0:
        return 0
    sum = 0
    for i in range(len(nums)):
        if nums[i] != 13:
            sum += nums[i]
            if (i > 0 and nums[i - 1] == 13):
                sum -= i
    return sum

def sum67(nums):
    # code later