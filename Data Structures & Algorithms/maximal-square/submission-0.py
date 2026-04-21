class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if r >= ROWS or c>=COLS:
                return 0
            if (r,c) not in cache:
                right = dfs(r, c+1)
                down = dfs(r+1, c)
                diag = dfs(r+1, c+1)
                cache[(r,c)] = 0
                if matrix[r][c] == '1':
                    cache[(r,c)] = 1 + min(right, down, diag)
            return cache[(r,c)]
        dfs(0,0)
        return max(cache.values()) ** 2