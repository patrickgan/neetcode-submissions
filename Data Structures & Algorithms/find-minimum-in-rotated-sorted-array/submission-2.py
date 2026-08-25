"""
Approach:
Binary search to find the pivot.
* Edge case: rotated n times, where min is nums[0] and max is nums[-1]
* In this case, the final ele > first ele, which lets us just return nums[0]

we could add elements to the array?

invariant: nums[i] < nums[j] for all i < j, in the original array

in cases where we haven't found the solution and must choose between two
subarrays, we go for the subarray that violates the invariant.

1234567 => return 1

234[5]671 => 671 2 < 5, 5 > 1
345[6]712 => 345 vs 712
456[7]123 => 456 vs 123
567[1]234 => return 1
671[2]345 => 671 vs 345
1 ... 7: if final ele > first ele, then it's not rotated.
2 ... 1
3 ... 2

12
21

if nums[pivot] < nums[pivot-1]: return

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[right] > nums[left]:
                return nums[left]
            pivot = (right - left) // 2 + left
            if nums[pivot] < nums[pivot-1]:
                return nums[pivot]
            elif nums[left] <= nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return nums[0]
                