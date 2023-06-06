def threeSumClosest(nums, target):
    nums.sort()

    # default to first 3 nums
    closest = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        # skip duplicates
        if i != 0 and nums[i - 1] == nums[i]:
            continue

        # perform two-sum II
        j, k = i + 1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total == target:
                return total
            # minimize closest by finding the smallest difference between the sum and target
            elif abs(target - total) < abs(target - closest):
                closest = total

            if total > target:
                k -= 1
            else:
                j += 1

    return closest

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], 1))