class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for task in tasks:
            freqMap[task] = freqMap.get(task, 0) + 1
        
        maxHeap = [-c for c in freqMap.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt!=0:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time