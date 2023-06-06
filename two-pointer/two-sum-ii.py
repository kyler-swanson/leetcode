def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return [l + 1, r + 1]
        elif total > target:
            r -= 1
        else:
            l += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))