"""
Approach:

hashing/dictionary sounds good

pass 1:
insert words into dictionaries.
    if an anagram does not have a corresponding key in the dict, insert it
    if it does, append it to the list of anagrams associated with the key
for key in dictionary:
    populate sublist
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        result = []
        for s in strs:
            key = self.sortLetters(s)
            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
        for key in anagrams:
            result.append(anagrams[key])
        return result
    def sortLetters(self, s):
        chars = [0 for i in range(0, 26)]
        result = ""
        for char in s:
            chars[ord(char) - ord('a')] += 1
        for order in range(0,26):
            result += chr(order) * chars[order]
        return result