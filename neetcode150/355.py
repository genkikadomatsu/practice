from typing import List

class Tweet:
    """Represents a Tweet."""

    def __init__(self, id: int, time: int):
        self.id = id
        self.time = time

    def __lt__(self, other) -> bool:
        return self.time < other.time

    def __le__(self, other) -> bool:
        return self.time <= other.time
    
    def __gt__(self, other) -> bool:
        return self.time > other.time
    
    def __ge__(self, other) -> bool:
        return self.time >= other.time


class User:
    """Represents a Twitter user."""

    def __init__(self, id: int):
        """Initialize a user."""

        self.id = id
        self.tweets: list[Tweet] = []
        self.following: list[User] = list()

    def post(self, id: int, time: int) -> None:
        """Adds tweet to user's tweet list."""

        self.tweets.append(Tweet(id, time))

class Twitter:

    def __init__(self):
        self.userIds = set()
        self.users = {}
        self.tweet_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Add a tweet for a user. If the user doesn't exist make it."""

        self.tweet_time += 1  
        user = self.users.get(userId, User(userId))
        user.tweets.append(Tweet(tweetId, self.tweet_count))

    def getNewsFeed(self, userId: int) -> List[int]:
        pass        
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.append(self.users[followeeId])
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)