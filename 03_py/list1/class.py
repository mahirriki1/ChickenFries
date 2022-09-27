def first_last6():
    

print(first_last6([1, 2, 6]) == True)
print(first_last6([6, 1, 2, 3]) == True)
print(first_last6([13, 6, 1, 2, 3]) == False)

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
    return [3,1,4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    count = 0
    for num in nums:
        count += num
    return count

def rotate_left3(nums):
    arr = []
    for i in range(len(nums)):
        if i != len(nums) - 1:
            arr.append(nums[0])
    return arr

def reverse3(nums): # return arr[::-1] works too
    arr = []
    for num in nums:
        arr.insert(0, num)
    return arr

def max_end3(nums):
    max_num = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = max_num
    return nums

def sum2(nums):
    if len(nums) == 0:
        return 0
    count = 0
    length = min(len(nums), 2)
    for i in range(length):
        count += nums[i]
    return count

def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3