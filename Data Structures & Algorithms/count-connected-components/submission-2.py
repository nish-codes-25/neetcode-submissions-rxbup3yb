class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return 0

            visit.add(node)
            for nei in adj[node]:
                if nei==parent:
                    continue
                if not dfs(nei, node):
                    continue
            return 1
        
        cnt = 0
        i = 0
        while i<n and len(visit)!=n:
            cnt += dfs(i, -1)
            i+=1

        return cnt

        
                
