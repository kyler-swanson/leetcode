def maxSubstringWithReplacement(s, k):
    start = 0

    substring = {}

    max_len = 0

    for end in range(len(s)):
        end_char = s[end]

        substring[end_char] = substring.get(end_char, 0) + 1

        while len(substring) >= k:
            