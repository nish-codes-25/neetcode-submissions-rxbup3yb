class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visit = set()
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
        
        cnt = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                cnt += 1
        return cnt

        
                
