def maxSum(nums, k) -> int:
  start, end = 0, 0
  
  sum = 0
  maxSum = 0

  for end in range(len(nums)):
    sum += nums[end]

    if end >= k - 1:
      if sum > maxSum:
        maxSum = sum

      sum -= nums[start]
      start += 1

  return maxSum

print(maxSum([2, 3, 4, 1, 5], 2))