def twoSum(nums, target):
    hm = {}

    for i, num in enumerate(nums):
        if num in hm:
            return [hm[num], i]
        else:
            hm[target - num] = i

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))