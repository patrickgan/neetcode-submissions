import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                second = stack.pop(-1)
                first = stack.pop(-1)
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    quotient = first / second
                    stack.append(math.trunc(quotient))
            else:
                stack.append(int(token))
        return stack[-1]