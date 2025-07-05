# leetcode 125
# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Time Complexity:
# Space Complexity:
def validPalindrome(s):
    cleanstring = ''.join(char for char in s if char.isalnum())
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