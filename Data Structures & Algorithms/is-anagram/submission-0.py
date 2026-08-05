from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter()
        for c in s:
            s_dict[c] += 1
        for c in t:
            s_dict[c] -= 1
        for key in s_dict.keys():
            if s_dict[key] != 0:
                return False
        return True