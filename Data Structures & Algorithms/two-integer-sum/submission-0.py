class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = dict()
        for i in range(0, len(nums)):
            num = nums[i]
            if num in bank:
                return [bank[num], i]
            else:
                bank[target - num] = i
        return [-1, -1]