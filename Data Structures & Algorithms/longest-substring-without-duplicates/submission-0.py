"""
6/22/26 10:50am
ran into bugs at 11:05am
gave up 11:21 am

sliding window approach
use a counter to help

sample:
"xyz"
"xyx"
"abab"
"xxx"

for length of input string:
    if all counts <= 1, increment right pointer
        if right - left > max, then max = right - left
    else, increment left pointer
return max

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        charSet = set()
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len