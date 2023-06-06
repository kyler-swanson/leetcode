def threeSum(nums):
    ans = []

    nums.sort()

    for i in range(len(nums) - 2):
        # skip duplicates
        if i != 0 and nums[i-1] == nums[i]:
            continue

        # perform two sum II on remainder of arr
        j, k = i + 1, len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1

                # skip any subsequent duplicates for j
                while nums[j - 1] == nums[j] and j < k:
                    j += 1
            elif total > 0:
                k -= 1
            else:
                j += 1

    return ans

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))