# leetcode 647
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Time Complexity:
# Space Complexity:

def palindromicSubstrings(s):
    text = s
    length = len(text)
    total = 0

    def expand_around_center(left_idx, right_idx):
        count = 0
        while (
                left_idx >= 0
                and right_idx < length
                and text[left_idx] == text[right_idx]
        ):
            count += 1
            left_idx -= 1
            right_idx += 1
        return count

    for center_idx in range(length):
        total += expand_around_center(center_idx, center_idx)
        total += expand_around_center(center_idx, center_idx + 1)

    return total