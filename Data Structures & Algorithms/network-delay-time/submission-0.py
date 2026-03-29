class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((v, t))
        print(adj)
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = t1

            for n2, t2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1+t2, n2))

        for i in range(1, n+1):
            if i not in visit:
                return -1

        return t



        
