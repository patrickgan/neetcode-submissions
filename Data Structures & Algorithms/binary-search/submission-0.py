"""
1 (3) 5 7 => len 4 => (3-0)/2 + 0 => pivot 1
* target = 5
* L: 0, R: 3, P: 1 | [1 (3) 5 7]
* L: 1, R: 3, P: 2 |
2 4 (6) 7 8 => len 5 => (4-0)/2 + 0 => pivot 2

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (right - left) // 2 + left
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1