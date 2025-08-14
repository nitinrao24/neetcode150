# leetcode 208
# A trie (pronounced as "try") or prefix tree is a tree data structure
# used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.

# Time Complexity:
# Space Complexity:

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:

        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur['*'] = ''

    def search(self, word: str) -> bool:

        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return '*' in cur

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True