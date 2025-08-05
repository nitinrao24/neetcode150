# leetcode 91
# Given a string s containing only digits,
# return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# Time Complexity:
# Space Complexity:

def decodeWays(s):
    # if the string starts with '0', there are no valid decodings
    if s[0] == '0':
        return 0

    length = len(s)

    # ways[i] will store the number of ways to decode up to position i
    ways = [0] * (length + 1)
    ways[0] = 1
    ways[1] = 1

    for pos in range(2, length + 1):
        # single digit decode (last one digit)
        single = int(s[pos - 1])
        # two-digit decode (last two digits)
        pair = int(s[pos - 2: pos])

        # if the single digit is between 1 and 9, it can form a valid letter
        if 1 <= single <= 9:
            ways[pos] += ways[pos - 1]

        # if the pair forms a number between 10 and 26, it can form a valid letter
        if 10 <= pair <= 26:
            ways[pos] += ways[pos - 2]

    # total ways to decode the entire string
    return ways[length]

print(decodeWays('226'))