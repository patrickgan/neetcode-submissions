"""
Approaches

Prefix product and suffix product arrays.
For every index i > 0, the prefix product will be the product of all indices 0 to i-1 (default 1)
For every index i < len(nums) - 1, the suffix product will be the product of all indices i+1 to len(nums) - 1 (default 1)

Therefore, to calculate the full product array, each index i will be prefix[i] * suffix[i].

Test cases:
1 2 3 5 (product 30)
1 2 0 5 (product 0)
-1 2 -1 0 (product 0)

Result:
30 15 10 6
prefix: [1] 1 2 6
suffix: 30 15 5 [1]

0 0 10 0
prefix: [1] 1 2 0
suffix: 0 0 5 [1]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        result = [1 for i in range(len(nums))]
        
        pre_product = 1
        post_product = 1
        # prefix pass
        for i in range(1, len(nums)):
            pre_product *= nums[i-1]
            prefix[i] = pre_product
        for i in range(0, len(nums)-1):
            j = len(nums)-i-2
            post_product *= nums[j+1]
            suffix[j] = post_product
        for i in range(0, len(nums)):
            result[i] = prefix[i] * suffix[i]
        return result