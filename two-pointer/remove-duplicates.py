def removeDuplicates(nums):
    l, r = 1, 1

    while r < len(nums):
        if nums[r - 1] != nums[r]:
            nums[l] = nums[r]
            l += 1
        r += 1
    
    return l

arr = [1,1,2]
print(removeDuplicates(arr), arr)

arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(arr), arr)