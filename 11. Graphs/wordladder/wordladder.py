# leetcode 127
# Given two words, beginWord and endWord, and a dictionary wordList,
# return the number of words in the shortest transformation sequence from beginWord to endWord,
# or 0 if no such sequence exists.

# Time Complexity:
# Space Complexity:
from typing import List
import string
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # Turn the word list into a set so we can check words super quickly
    word_set = set(wordList)

    # If endWord isn’t in our set, we can’t transform into it
    if endWord not in word_set:
        return 0

    # We’ll do a two-way search—from the start and the end—so we meet in the middle
    front = {beginWord}
    back = {endWord}
    visited = set()   # keep track of words we’ve already tried
    steps = 1         # how many transformations we’ve done so far

    # Keep going as long as both sides still have words to explore
    while front and back:
        # Always expand the smaller side to save work
        if len(front) > len(back):
            front, back = back, front

        next_front = set()  # where we’ll collect the next batch of words

        # For each word we can reach right now...
        for word in front:
            # try changing each letter in the word
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue

                    # build a new candidate word
                    new_word = word[:i] + c + word[i+1:]

                    # if this new word hits the other search side, we’re done
                    if new_word in back:
                        return steps + 1

                    # if it’s a real word we haven’t seen yet, add it to the next round
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        next_front.add(new_word)

        # move on to the next step
        front = next_front
        steps += 1

    # if we exhaust one side without meeting, there’s no path
    return 0