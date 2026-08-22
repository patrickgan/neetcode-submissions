"""
total # entries = m * n (where m = number of rows, n = number of entries in each row)
coords (i,j) of element k (zero-indexed): 
    i = k // n
    j = k - (i * n)
then, execute normal binary search
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n - 1

        while left <= right:
            pivot = (right - left) // 2 + left
            i = pivot // n
            j = pivot - (i * n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return False
            