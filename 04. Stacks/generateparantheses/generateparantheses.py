# leetcode 22
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Time Complexity: O(n) per result
# Space Complexity: O(n)

def generateParantheses(n):
    results = []

    def rucursion(val, front, back):
        if len(val) == 2 * n:
            results.append(val)
            return
        if front < n:
            rucursion(val + "(", front + 1, back)
        if front > back:
            rucursion(val + ")", front, back + 1)

    rucursion("", 0, 0)
    return results

print(generateParantheses(3))
print(generateParantheses(1))