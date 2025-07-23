# leetcode 125
# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Time Complexity: O(n)
# Space Complexity: O(1)

def validPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): # isalnum() referring to whether the character is alphanumeric or not
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def validPalindrome1(s):
    cleanstring = ''.join(char for char in s if char.isalnum()) # skips alphanumeric characters
    cleanstring = cleanstring.lower()
    start = 0
    end = len(cleanstring) - 1
    while start < end:
        if cleanstring[start] == cleanstring[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("Race a car"))
print(validPalindrome(""))