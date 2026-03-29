class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -num)
            return

        if len(self.maxHeap) > len(self.minHeap):
            if num>=-self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                maximum = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, -num)
                heapq.heappush(self.minHeap, maximum)
        elif len(self.maxHeap)==len(self.minHeap):
            if num <= self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                maximum = heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -maximum)
        return None

    def findMedian(self) -> float:
        if len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0])/2
        