class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS  = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addBanana(r, c):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or grid[r][c]==0:
                return

            q.append([r,c])
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))

        time = -1

        while q:
            print(q)
            for i in range(len(q)):    
                r, c = q.popleft()
                grid[r][c] = 2
                addBanana(r+1, c)
                addBanana(r-1, c)
                addBanana(r, c+1)
                addBanana(r, c-1)
            time += 1
        
        elements = set()
        for row in grid:
            elements.update(set(row))
        if 1 in elements:
            return -1
        elif elements=={0}:
            return 0
        return time



        