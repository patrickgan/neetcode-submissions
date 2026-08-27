"""
Approach
Modified binary search

123567 -- search 4
356712 -- search 4

Non-rotated
1[2]34 -- search 5
-> 5 is greater than biggest element, so we return -1

12[3]56 -- search 4
-> 4 is greater than pivot, so we check the right half... but it's also less than the
smallest element on the right half, so we can return -1

23[5]67 -- search 4
-> 4 is less than pivot, so we check left half, but it's greater than the biggest
element on left half, so we return -1

For a non-rotated array, this is a somewhat standard binary search.
---
Rotated arrays:

check for rotation by checking nums[end] and nums[begin]. if end > begin, not rotated. if end < begin, then it is rotated
```
isRotated = nums[end] < nums[begin]
```

105 ... 999 1 [2] 3 ... 104 -- search 107
-> isRotated 
-> 107 > nums[left], so check left half
-> 105 ... 499 [500] ... 999 1 -- search 107
-> 107 > nums[left], so check left half
-> 105 ... [250] ... 499
-> not rotated
-> standard binary search

105 ... [250] ... 499 -- search 107
105 ... [250] ... 499 -- search 251
---
Rotated array AND it doesn't exist

"Between last and first"
106 .. 999 1 [2] 3 .. 104 -- search 105
-> isRotated
-> 105 > 104, 105 < 106
-> 105 > nums[right] AND 105 < nums[left], return -1

"Somewhere in the middle"
105 .. 999 1 [2] 3 .. 104 -- search 1000
-> isRotated
-> 1k > 105, so check left half
-> 105 .. 498 .. 999 1 -- search 1000
-> 1k > 105, so check left half??
-> 105 .. 497

"Somewhere in the middle but it does exist"
105 .. 999 1 [2] 3 .. 104 -- search 999
-> isRotated
-> 999 > 105, so check left half
-> 105 .. 498 .. 999 1 -- search 999
-> 999 > 105, so check left half??
-> 105 .. 497
---
Easier to just find the point of rotation first in one pass, then binary search the correct one of two segments in a second pass.


(>2) (105 .. 999 1) [2] 3 .. 104 .. (>2)
(<900) .. [900] (901 .. 999 1 ..) (<900)

rotation_check_find_minimum_binary_search {
    left, right = 0, len(nums)-1
    while left < right:
        pivot = (right-left) // 2 + left
        if nums[pivot] < nums[pivot-1]:
            return pivot
        elif nums[right] > nums[pivot]:
            Check Left
        elif nums[right] < nums[pivot]:
            Check Right
}

105 .. 999; 1 .. 104 | search 4
if target < nums[right], search right array [pivot:end]

105 .. 999; 1 .. 104 | search 500
if target > nums[right], search left array [0:pivot]

unrotated_binary_search {
    left, right = 0, len(nums) - 1
    while left < right:
        if target > biggest or target < smallest:
            return -1
        pivot = ( right - left ) // 2 + left
        if target == nums[pivot]:
            return pivot
        elif target > nums[pivot]:
            left = pivot + 1
        else:
            right = pivot - 1
    ...
}
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        if nums[left] > nums[right]:
            # Search for rotation point, store index of minimum
            while left < right:
                pivot = (right - left) // 2 + left
                if nums[pivot] < nums[pivot-1]:
                    break
                elif nums[right] > nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            pivot = (right - left) // 2 + left
            min_point = pivot

            if target <= nums[-1]:
                left = min_point
                right = len(nums) - 1
            else:
                left = 0
                right = min_point - 1

        while left < right:
            if target < nums[left] or target > nums[right]:
                return -1
            pivot = (right - left) // 2 + left
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        
        if nums[left] == target:
            return left
        return -1
