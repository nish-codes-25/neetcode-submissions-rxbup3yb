class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        print(adj)
        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < N:
            print(minHeap)
            dist, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += dist
            visit.add(node)
            for neiDist, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiDist, nei])
        return res
