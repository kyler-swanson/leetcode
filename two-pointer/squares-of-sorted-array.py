def sortedSquares(nums):
    res = []

    l, r = 0, len(nums) - 1

    while l <= r:
        left_square = nums[l] * nums[l]
        right_square = nums[r] * nums[r]

        if left_square > right_square:
            res.append(left_square)
            l += 1
        else:
            res.append(right_square)
            r -= 1

    return reversed(res)

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))