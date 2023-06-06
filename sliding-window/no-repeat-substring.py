def lengthOfLongestSubstring(s):
    start = 0

    substring = {}

    max_len = 0

    for end in range(len(s)):
        end_char = s[end]

        substring[end_char] = substring.get(end_char, 0) + 1

        while substring[end_char] > 1:
            start_char = s[start]
            
            substring[start_char] -= 1
            if substring[start_char] == 0:
                del substring[start_char]

            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len
        
print(lengthOfLongestSubstring("aabccbb"))
print(lengthOfLongestSubstring("abbbb"))
print(lengthOfLongestSubstring("abccde"))