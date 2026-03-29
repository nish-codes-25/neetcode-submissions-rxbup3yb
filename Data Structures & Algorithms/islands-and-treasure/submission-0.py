class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or grid[r][c]==-1:
                return
            q.append([r,c])
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r, c+1)
                addRoom(r-1, c)
                addRoom(r, c-1)
            dist += 1

                

"""
[inf,  -1,   0, inf]
[inf, inf, inf,  -1]
[inf,  -1, inf,  -1]
[0,    -1, inf, inf]
"""
