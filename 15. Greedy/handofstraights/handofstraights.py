# leetcode 846
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
# and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.
from collections import Counter
# Time Complexity:
# Space Complexity:
def handOfStraights(hand,groupSize):
    cards = hand
    size = groupSize

    if len(cards) % size != 0:
        return False

    freq = Counter(cards)
    unique_vals = sorted(freq.keys())

    for val in unique_vals:
        if freq[val] > 0:
            needed = freq[val]
            for num in range(val, val + size):
                if freq[num] < needed:
                    return False
                freq[num] -= needed

    return True

