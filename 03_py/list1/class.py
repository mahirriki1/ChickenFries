def first_last6(nums):
    return nums[0]==6 or nums[-1]==6

print(first_last6([1, 2, 6]) == True)
print(first_last6([6, 1, 2, 3]) == True)
print(first_last6([13, 6, 1, 2, 3]) == False)

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

print(same_first_last([1, 2, 1]) == True)
print(same_first_last([7]) == True)
print(same_first_last([]) == False)

def make_pi():
    return [3,1,4]

print(make_pi() == [3, 1, 4])

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

print(common_end([1, 2, 3], [7, 3]) == True)
print(common_end([1, 2, 3], [7, 3, 2]) == False)
print(common_end([1, 2, 3], [1, 3]) == True)

def sum3(nums):
    count = 0
    for num in nums:
        count += num
    return count

print(sum3([1, 2, 3]) == 6)
print(sum3([5, 11, 2]) == 18)
print(sum3([7, 0, 0]) == 7)

def rotate_left3(nums):
    arr = []
    for i in range(len(nums)):
        if i != len(nums) - 1:
            arr.append(nums[0])
    return arr

print(rotate_left3([1, 2, 3]) == [2, 3, 1])
print(rotate_left3([5, 11, 9]) == [11, 9, 5])
print(rotate_left3([7, 0, 0]) == [0, 0, 7])

def reverse3(nums): # return arr[::-1] works too
    arr = []
    for num in nums:
        arr.insert(0, num)
    return arr

print(reverse3([1, 2, 3]) == [3, 2, 1])
print(reverse3([5, 11, 9]) == [9, 11, 5])
print(reverse3([7, 0, 0]) == [0, 0, 7])

def max_end3(nums):
    max_num = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = max_num
    return nums

print(max_end3([1, 2, 3]) == [3, 3, 3])
print(max_end3([11, 5, 9]) == [11, 11, 11])
print(max_end3([2, 11, 3]) == [3, 3, 3])

def sum2(nums):
    if len(nums) == 0:
        return 0
    count = 0
    length = min(len(nums), 2)
    for i in range(length):
        count += nums[i]
    return count

print(sum2([1, 2, 3]) == 3)
print(sum2([1, 1]) == 2)
print(sum2([1, 1, 1, 1]) == 2)

def middle_way(a, b):
    return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]) == [2, 5])
print(middle_way([7, 7, 7], [3, 8, 0]) == [7, 8])
print(middle_way([5, 2, 9], [1, 4, 5]) == [2, 4])

def make_ends(nums):
    return [nums[0], nums[-1]]

print(make_ends([1, 2, 3]) == [1, 3])
print(make_ends([1, 2, 3, 4]) == [1, 4])
print(make_ends([7, 4, 6, 2]) == [7, 2])

def has23(nums):
    return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3

print(has23([2, 5]) == True)
print(has23([4, 3]) == True)
print(has23([4, 5]) == False)