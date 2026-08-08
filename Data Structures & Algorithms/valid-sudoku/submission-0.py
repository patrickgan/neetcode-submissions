"""
Approach:

Row check
* could use a set
Col check
* could just transpose the list
Box check
* could use a helper. we have 9 boxes.

squareFinder
1,1 => 0
4,5 => 4
2,0 => 0
6,6 => 8

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        # row check
        for i in range(9): # for each row
            for j in range(9): # for each col
                val = board[i][j]
                k = self.squareFinder(i,j)                
                if val == ".":
                    continue
                if val in rows[i] or val in cols[j] or val in squares[k]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[k].add(val)
        return True
    
    def squareFinder(self, row, col):
        return 3 * (row // 3) + col // 3