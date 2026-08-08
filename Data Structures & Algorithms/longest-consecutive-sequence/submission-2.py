"""
Approach:
Sort the list, then do a linear pass.
...Except this should be done in linear time.

A few strategies come to mind regarding linear structures and algorithms:
* multiple passes
* prefix array
* hash maps

Constraintss:
nums has length of up to 100,000
nums[i] can be anything from -10^9 to 10^9
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set((nums))))
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                current = 1
            else:
                current += 1
                if current > longest: 
                    longest = current
        return longest