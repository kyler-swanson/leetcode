def dutchFlag(nums):
    def swap(nums, one, two):
        tmp = nums[one]
        nums[one] = nums[two]
        nums[two] = tmp

    l, mid, r = 0, 0, len(nums) - 1

    while mid <= r:
        if nums[mid] == 0:
            swap(nums, l, mid)
            l += 1
            mid += 1
        elif nums[mid] == 2:
            swap(nums, mid, r)
            r -= 1
        else:
            mid += 1

nums = [2, 0, 0, 1, 2, 1]
dutchFlag(nums)

print(nums)

nums = [2, 0, 1]
dutchFlag(nums)

print(nums)