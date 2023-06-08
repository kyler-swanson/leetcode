def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)

        if area > max_area:
            max_area = area

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1