# checks if 2 strings are anagrams of one another
# leetcode 217
def validAnagram(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        return True
    else:
        return False

s = "rat"
t = "car"
output = validAnagram(s, t)
print(output)