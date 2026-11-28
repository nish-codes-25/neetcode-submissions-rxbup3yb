class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l,r = 0, ROWS*COLS - 1

        while l <= r:
            h = (r+l)//2
            row, col = h//COLS, h%COLS
            if target < matrix[row][col]:
                r = h-1
            elif target > matrix[row][col]:
                l = h+1
            else:
                return True
        return False