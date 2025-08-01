# leetcode 17
# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

# Time Complexity:
# Space Complexity:

def letterCombinations(digits):
    if not digits:
        return []

    letters_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    combinations = []

    def backtrack(index, prefix):
        if index == len(digits):
            combinations.append(prefix)
            return
        digit = digits[index]
        for letter in letters_map[digit]:
            backtrack(index + 1, prefix + letter)

    backtrack(0, "")
    return combinations

print(letterCombinations("23"))