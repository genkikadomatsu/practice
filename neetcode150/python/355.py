from typing import List
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set) # {userId: {userId2, ...}}
        self.user_posts = defaultdict(list)  # {userId: [(time, tweetId1), ...]}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_posts[userId].append((self.time, tweetId))
        self.user_follows[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        
        following = self.user_follows[userId]
        allPosts = []

        for i, user in enumerate(following):
            allPosts.extend(self.user_posts[user])

        allPosts.sort(key=lambda x: x[0], reverse=True) 
        return [x[1] for x in allPosts[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
