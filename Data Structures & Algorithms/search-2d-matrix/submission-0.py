class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])-1

        n = len(matrix[0])

        while l<=r:
            mid = (l+r)//2
            i, j = (mid)//n, (mid)%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False