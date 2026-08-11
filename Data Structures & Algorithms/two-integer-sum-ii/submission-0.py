"""
Typical solution for 2-Sum is to use a dictionary for O(n) runtime, but would take O(n) additional space.
Notably, this list is sorted, which allows us to use a two-pointer approach.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            result = numbers[head] + numbers[tail]
            if result == target:
                return [head+1,tail+1]
            elif result < target:
                head += 1
            else:
                tail -= 1
        return [-1,-1]