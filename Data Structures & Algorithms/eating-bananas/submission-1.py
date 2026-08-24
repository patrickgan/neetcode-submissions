"""
to calculate total hours:
hours = sum(piles[i] / k for all i in range(len(piles)))
if hours == h, return that k
if hours > h, we're eating too slowly. increase k.
if hours < h, we check if we can eat slower. store best k, then decrease k.

do a binary search
w/ stopping condition: 
hours = target h
or left > right.
pivot represents the rate at each time

"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        best_k = max(piles)
        while left <= right:
            k = (right - left) // 2 + left
            hours = sum([math.ceil(bananas / k) for bananas in piles])
            if hours <= h:
                best_k = min(best_k, k)
                right = k - 1
            else:
                left = k + 1
        return best_k