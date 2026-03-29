class Twitter:

    def __init__(self):
        self.connection = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.connection[userId].add(userId)
        for following in self.connection[userId]: 
            if following in self.tweets: 
                index = len(self.tweets[following]) - 1
                count, tweetId = self.tweets[following][index]
                minHeap.append([count, tweetId, following, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, following, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[following][index]
                heapq.heappush(minHeap, [count, tweetId, following, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.connection[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connection[followerId]:
            self.connection[followerId].remove(followeeId) 



