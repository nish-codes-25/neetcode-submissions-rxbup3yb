class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append((self.count, tweetId))
        
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee])-1
                cnt, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [cnt, tweetId, followee, index-1])
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        res = []
        while minHeap and len(res)!=10:
            cnt, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                cnt, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [cnt, tweetId, followee, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
