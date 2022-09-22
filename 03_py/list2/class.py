def count_evens(nums):
    count = 0 
    for num in nums:
        if num % 2 == 0: # if num is divisble by 2
            count += 1
    return count

print(count_evens([2, 1, 2, 3, 4]) == 3)
print(count_evens([2, 2, 0]) == 3)
print(count_evens([1, 3, 5]) == 0)
print(count_evens([]) == 0)

def big_diff(nums):
    small = nums[0]
    big = nums[0]
    for num in nums: # this loop finds the smallest and biggest number in array
        small = min(small, num) 
        big = max(big, num)
    return big - small

print(big_diff([5, 1, 6, 1, 9, 9]) == 8)
print(big_diff([7, 6, 8, 5]) == 3)
print(big_diff([7, 7, 6, 8, 5, 5, 6]) == 3)

def centered_average(nums):
    small = nums[0]
    big = nums[0]
    for num in nums:
        small = min(small, num)
        big = max(big, num)
    sum = 0
    for num in nums:
        sum += num
    return (sum - (small + big)) / (len(nums) - 2) # total sum being subtracted from the sum of the small and big divided by the total length - 2

print(centered_average([1, 2, 3, 4, 100]) == 3)
print(centered_average([1, 1, 5, 5, 10, 8, 7]) == 5)
print(centered_average([-10, -4, -2, -4, -2, 0]) == -3)

def sum13(nums):
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i != len(nums) - 1: # 2nd condition so theres no out of bounds error
                nums[i + 1] = 0
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sum13([1, 2, 2, 1]) == 6)
print(sum13([1, 1]) == 2)
print(sum13([1, 2, 2, 1, 13]) == 6)
print(sum13([]) == 0)

def sum67(nums):
    sum = 0
    i = 0
    while i < len(nums):
        if nums[i] == 6:
            while nums[i] != 7: # to skip over the values in between 6 and 7 inclusive
                i += 1
            i += 1
        if i < len(nums) and nums[i] != 6: # this adds to the sum
            sum += nums[i]
            i += 1
    return sum

print(sum67([1, 2, 2]) == 5)
print(sum67([1, 2, 2, 6, 99, 99, 7]) == 5)
print(sum67([1, 1, 6, 7, 2]) == 4)

def has22(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 2:
            if i != len(nums) - 1 and nums[i + 1] == 2: # first condition is for no out of bounds error
                return True
            i += 1
        else:
            i += 1
    return False

print(has22([1, 2, 2]) == True)
print(has22([1, 2, 1, 2]) == False)
print(has22([2, 1, 2]) == False)
        