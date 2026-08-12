"""
Approach:
Sliding window. Keep track of duplicates with a counter or set.

Keep expanding the window until we hit a duplicate, or reach the end of the string.
While we have a duplicate, and the left side of the window hasn't reached the end of the string, 
we progress the left side of the window.

abaxxxxx => 3
xxxx => 1
"""

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        counter = Counter()
        longest = 0
        while r < len(s):
            c = s[r]
            counter[c] += 1
            r += 1
            if counter[c] == 1 and r - l > longest:
                longest = r - l
            while counter[c] > 1:
                counter[s[l]] -= 1
                l += 1
        return longest
