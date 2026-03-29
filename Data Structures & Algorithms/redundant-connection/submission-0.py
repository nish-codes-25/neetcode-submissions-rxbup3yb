class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visit = [False]*(n+1)
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                x= dfs(nei, node)
                print(nei, node, par, cycle, cycleStart, x)
                if x:
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1 
                    return True
            return False
        
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []

