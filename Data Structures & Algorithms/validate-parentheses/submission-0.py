"""
Use a stack.
Each left paren pushes to the stack, and each right paren must match with the most recently pushed left paren.
Each valid right paren removes the most recent left paren from the stack.
If the stack is empty and we get a right paren, we return false.
If the stack is not empty by the end of the string, we return false.
If all the other conditions have been properly met, and the stack is empty at the end of the string, we return true.

We use a dictionary to simplify lookup.

({[]})
({]})
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parens = {')': '(', '}': '{', ']':'['}
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if len(stack) == 0:
                    return False
                d = stack.pop()
                if d != parens[c]:
                    return False
        if len(stack) > 0:
            return False
        return True