# leetcode 355
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
# Implement the Twitter class:
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
# Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
# Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

# Time Complexity:
# Space Complexity:

from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.tweets = []
        self.follow_map = defaultdict(set)

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.follow(user_id, user_id)
        self.tweets.append((user_id, tweet_id))

    def getNewsFeed(self, user_id: int) -> List[int]:
        feed = []
        follows = self.follow_map.get(user_id, set())
        for author_id, tid in reversed(self.tweets):
            if author_id in follows:
                feed.append(tid)
                if len(feed) == 10:
                    break
        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].discard(followee_id)