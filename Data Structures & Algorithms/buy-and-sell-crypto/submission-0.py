"""
Approach:
prefix/suffix arrays
lowest price prefix, highest price suffix

215697
prefix: 211111
suffix: 999997
max profit: 8
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = [prices[0] for price in prices]
        suffix = [prices[-1] for price in prices]
        for i in range(1, len(prices)):
            prefix[i] = min(prices[i], prefix[i-1])
        for i in range(len(prices)-2, -1, -1):
            suffix[i] = max(prices[i], suffix[i+1])
        return max([0] + [suffix[i] - prefix[i] for i in range(0, len(prices))])