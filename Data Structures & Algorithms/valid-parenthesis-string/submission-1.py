"""
6/15/26 6:06pm

# Approach: #
opens = 0
stars = 0
every open adds 1, every close subtracts 1.
if we are not at 0 by the end, return false
if we hit -1 at any point, return false

stars change things a bit.
if we reach -1 at any point, we can remove a star to move it back to 0.
-1 with 0 stars returns false
if we are above 0 by the end, we can remove a star to move it back towards 0.

((**()**
((***( -- false

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Check left-to-right
        opens = 0
        stars = 0
        for char in s:
            if char == '(':
                opens += 1
            if char == ')':
                opens -= 1
                if opens == -1:
                    if stars == 0:
                        return False
                    else:
                        stars -= 1
                        opens += 1
            if char == '*':
                stars += 1
        if (opens - stars) > 0:
            return False
        # Check right-to-left
        opens = 0
        stars = 0
        for char in s[::-1]:
            if char == ')':
                opens += 1
            if char == '(':
                opens -= 1
                if opens == -1:
                    if stars == 0:
                        return False
                    else:
                        stars -= 1
                        opens += 1
            if char == '*':
                stars += 1
        return (opens - stars) <= 0
