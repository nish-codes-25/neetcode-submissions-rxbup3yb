class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x, y = points[i]
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap, [-dist, i])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            dist, index = heapq.heappop(heap)
            res.append(points[index])
        return res


        