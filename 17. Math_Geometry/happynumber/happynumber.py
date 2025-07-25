# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Time Complexity:
# Space Complexity:

def happyNumber(n):
    l = set()
    while True:
        if n == 1:
            return True

        sum = 0
        while n != 0:
            digit = n % 10
            sum += digit * digit
            n = n // 10

        n = sum
        if n not in l:
            l.add(n)
        else:
            return False

print(happyNumber(2))
print(happyNumber(19))