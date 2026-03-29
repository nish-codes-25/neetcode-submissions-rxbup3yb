class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while heap:
            if len(heap)==1:
                return abs(heap[0])
            elif len(heap)==0:
                return 0
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, s1 - s2)

            
