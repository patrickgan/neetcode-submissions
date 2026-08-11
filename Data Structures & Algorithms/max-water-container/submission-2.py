"""
Formula:
area_(i,j) = min(height_i, height_j) * (j - i)

Can't just iterate through all possible combinations, as that would be O(n^2) time.
How to decide between which combination to go to?
Maybe we keep going until we reach a higher height, then calculate from there,
as any less-extreme index with the same height will only return a smaller area.

How do we decide between moving the head and moving the tail?

1,1,1,1,1,100,100,1,1,1,1
1,1,1,1,100,1,1,1,1,100
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        head = 0
        tail = len(heights) - 1
        result = self.area(heights, head, tail)
        while head < tail:
            if heights[head] < heights[tail]:
                head += 1
            elif heights[head] > heights[tail]:
                tail -= 1
            else:
                head += 1
                tail -= 1
            result = max(result, self.area(heights, head, tail))
        return result

    def area(self, heights, i, j):
        assert(j > i, "Second height must come after first height.")
        return (j - i) * min(heights[i], heights[j])