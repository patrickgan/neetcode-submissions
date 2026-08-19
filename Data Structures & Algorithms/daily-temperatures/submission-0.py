"""

[93, 23, 91, 23, 100, 100, 99, 98]
[ 4,  1,  2,  1,   0,   0,  0,  0]

two-stack approach?

stack_all: stores temperatures from most recent to most old
stack_top: stores popped temperatures until we hit a higher temperature?

stack_all: [98, 99, 100, 100, 23, 91, 23, 93]

pop 93: [(93,0)] | [98, 99, 100, 100, 23, 91, 23, 93]
pop 23: [(93,0), (23, 1)] | 23 is not higher than 93
pop 91: [(93,0), (23, 1), (91, 2)] | 91 > 23, 91 !> 93 | [?, 1, ?, ...]
    * temperature, index = 91, 2
    * t, i = 23, 1 | result[1] = 2-1; current = [93]
    * t, i = 93, 0 | break; current = [93, 91]
..
pop 100: [(93,0), (91,2), (23,3), (100,4)] | 100 > 93 ... | [4, ]
    * temp, index = 100, 4
    * t, i = 23, 3 | current: 93, 91
    * ... | current: 93
    * ... | current: []
    * current: [(100, 4)]
...
pop 98: [(100,4), (100,5), (99,6), (98,7)] | [0,0,0,0]

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for temp in temperatures]
        stack = []
        current = []
        for i in range(len(temperatures)-1, -1, -1):
            stack.append((temperatures[i], i))
        while stack:
            temperature, index = stack.pop(-1)
            while current:
                t, i = current[-1]
                if t >= temperature:
                    break
                result[i] = index - i
                current.pop(-1)
            current.append((temperature, index))
        for temperature, i in current:
            result[i] = 0
        return result