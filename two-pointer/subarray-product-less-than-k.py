def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    num_smaller = 0

    l = 0
    product = 1

    for r in range(len(nums)):
        product *= nums[r]
        
        while product >= k:
            product /= nums[l]
            l += 1

        num_smaller += r - l + 1

    return num_smaller

print(numSubarrayProductLessThanK([10,5,2,6], 100)) # 8
print(numSubarrayProductLessThanK([1,2,3], 0)) # 0