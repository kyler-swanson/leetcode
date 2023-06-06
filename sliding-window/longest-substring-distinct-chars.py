def maxSubstringDistinct(str, k):
    start = 0

    substring = {}
    max_length = 0

    for end in range(len(str)):
        substring[str[end]] = substring.get(str[end], 0) + 1

        while len(substring) > k:
            substring[str[start]] -= 1
            if (substring[str[start]] == 0):
                del substring[str[start]]
                
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

print(maxSubstringDistinct("araaci", 2))
print(maxSubstringDistinct("araaci", 1))
print(maxSubstringDistinct("cbbebi", 3))