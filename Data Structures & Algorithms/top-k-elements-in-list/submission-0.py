"""
Approach:

Create a counter (element: count), then sort the counter keys by count. Return first k elements.
Runtime: O(n) and then O(n log n)
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter()
        for num in nums:
            counter[num] += 1

        all_nums_sorted = sorted(counter.keys(), key=lambda num : counter[num], reverse=True)

        return all_nums_sorted[0:k]