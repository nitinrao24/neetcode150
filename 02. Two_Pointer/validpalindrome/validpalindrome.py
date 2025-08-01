# leetcode 125
# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Time Complexity: O(n) since we have a outer while loop
# Space Complexity: O(1) since we use only two variables left and right.

def validPalindrome(s):
    left = 0  # Set left pointer to the beginning of the string (index 0)
    right = len(s) - 1 # Set right pointer to the end of the string (last index)
    while left < right:
        # While left is less than right AND character at left is not alphanumeric
        while left < right and not s[left].isalnum(): # isalnum() referring to whether the character is alphanumeric or not
            left += 1 # increment left pointer
        # While left is less than right AND character at right is not alphanumeric:
        while left < right and not s[right].isalnum():
            right -= 1 # decrement right pointer
        # compare lower case converted values at left and right
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True # Loop finishes so it is a palindrome.


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
