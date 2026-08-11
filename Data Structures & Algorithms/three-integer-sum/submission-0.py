"""
Approach
Treat this problem as multiple 2-sum problems.

index i: twoSum(nums, target), where:
* nums = nums[i+1:end]
* target = -1 * nums[i]
We don't include previous values of i in nums since they'll already have been accounted for.

Runtime is O(n^2), as we run two-sum n times.
Space is O(n^2) as well, since each run of two-sum takes O(n) space.

Sorting the array before starting allows us to do a two-pointer approach, and use O(1) extra space.
Runtime would be O(n^2), plus a negligible (for large numbers) O(n log n) for the sort.

[-1,0,-1,0,1,1]
[-1,-1,0,0,1,1] => -1,0,1
[-1,-1,2] => -1,-1,2
[-2,-1,0,1,1,2] => -2,1,1; -2,0,2

Duplicates:
Put the results into a set.

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()
        for i in range(0, len(nums)-2):
            subresults = self.twoSumSorted(nums[i+1:],-nums[i])
            for result in subresults:
                results.add((nums[i],result[0],result[1]))
        results = [list(result) for result in results]
        return results
        
    def twoSumSorted(self, nums, target):
        head = 0
        tail = len(nums) - 1
        results = set()
        while head < tail:
            result = nums[head] + nums[tail]
            if result == target:
                results.add((nums[head], nums[tail]))
                head += 1
                tail -= 1
            elif result < target:
                head += 1
            else:
                tail -= 1
        return results