from collections import defaultdict
from time import time

class Twitter:

    def __init__(self):
        self.userToTweetMap = defaultdict(list)
        self.userToFollowerMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToTweetMap[userId].append((time(), tweetId))
        print(self.userToTweetMap)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for tweet in self.userToTweetMap[userId]:
            tweets.append(tweet)
        followers = self.userToFollowerMap[userId]
        for follower in followers:
            for tweet in self.userToTweetMap[follower]:
                tweets.append(tweet)
        sortedTweets = [tweet[1] for tweet in sorted(tweets, reverse = True)]
        if len(sortedTweets) <= 10:
            return sortedTweets
        return sortedTweets[0:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userToFollowerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowerMap[followerId].discard(followeeId)
