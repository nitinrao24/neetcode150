# leetcode 271
# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.

# Time Complexity:
# Space Complexity:

class Solution:

    def encode(strs):
        encoded_result = ""
        for string in strs:
            length = len(string)
            encoded_result += str(length) + "#" + string
        return encoded_result

    def decode(s):
        result = []
        index = 0

        while index < len(s):
            hash_index = index
            while s[hash_index] != "#":
                hash_index += 1

            length = int(s[index:hash_index])

            start = hash_index + 1
            end = start + length

            result.append(s[start:end])

            index = end

        return result


