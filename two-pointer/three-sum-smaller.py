def threeSumSmaller(nums, target):
    num_smaller = 0

    nums.sort()

    for i in range(len(nums) - 2):
        if i != 0 and nums[i - 1] == nums[i]:
            continue

        j, k = i + 1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < target:
                num_smaller += k - j
                j += 1
            else:
                k -= 1

    return num_smaller

print(threeSumSmaller([3, 1, 7, 4, 5], 12)) # 4
print(threeSumSmaller([0, -2, 1, 3], 2)) # 2
print(threeSumSmaller([-2, 0, 1, 3], 2)) # 2