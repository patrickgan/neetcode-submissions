"""
Approach:
Sliding window. For each substring window, check if it's a permutation of s1.

Test cases:
aaa bbaaa (len 3 and 5)
start with window s2[0:3], end with window s2[2:5]
"""
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter = Counter()
        window = Counter()
        for i in range(0, len(s1)):
            c = s1[i]
            counter[c] += 1
        for i in range(0, len(s1)):
            c = s2[i]
            window[c] += 1
            if window == counter:
                return True
        for i in range(len(s1), len(s2)):
            c = s2[i]
            d = s2[i-len(s1)]
            window[d] -= 1
            window[c] += 1
            if window == counter:
                return True
        return False