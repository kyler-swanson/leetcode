import math

def minSubArrayLen(target: int, nums) -> int:
    start = 0
    window_sum = 0

    min_length = math.pow(10, 9)

    for end in range(len(nums)):
        window_sum += nums[end]

        while window_sum >= target:
            min_length = min(min_length, end - start + 1)

            window_sum -= nums[start]
            start += 1

    return 0 if min_length == math.pow(10, 9) else min_length

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))