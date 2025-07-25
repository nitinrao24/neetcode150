# leetcode 703
# You are part of a university admissions office
# and need to keep track of the kth highest test score from applicants in real-time.
# This helps to determine cut-off marks for interviews
# and admissions dynamically as new applicants submit their scores.
# You are tasked to implement a class which, for a given integer k,
# maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted.
# More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Time Complexity:
# Space Complexity:

class KthLargest:

    def __init__(self,k,nums):
        self.k = k
        self.scores = nums

    def add(self, val):
        self.scores.append(val)
        self.scores.sort()
        return self.scores[-self.k]