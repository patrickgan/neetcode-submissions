"""

Rainwater can only be trapped between two bars of non-zero height with some space between them, where the height
of bars in that space is less than that of either outer bar.


4314 - that's going to be 2*4 - 3 - 1  = 4
4315 => 4
431505314
0203101321

What if we start from the outside and go in?
Make a calculated guess on the area and update it as we go further in.

What if we store the value of the height of rainwater at each index? Or at least the highest L and R values discovered so far?
4315
rw_heights: x44x
areas calculated by rw_height - height[i]

431505314
rw_heights: 444555444
areas: 013050130

to calculate rw_height, need to calculate min of L and R


4315053150
start from the L, then go right:
left:
4445555555
start from R, then go left
right:
5555555550
calculate RW_height: min(L[i],R[i])
4445555550
calculate area: RW_height - height[i]
0130502400

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0] for h in height]
        right = [height[-1] for h in height]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i], right[i+1])
        rw_height = [min(left[i], right[i]) for i in range(0, len(height))]
        trapped = [rw_height[i] - height[i] for i in range(0, len(height))]
        return sum(trapped)