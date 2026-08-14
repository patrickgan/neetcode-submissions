"""
Approach:
Store the min at each point in the stack.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minima = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minima) == 0:
            self.minima.append(val)
        else:
            self.minima.append(min(val,self.minima[-1]))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.minima.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minima[-1]
