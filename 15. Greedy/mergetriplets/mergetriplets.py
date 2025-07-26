# leetcode 1899
# A triplet is an array of three integers. You are given a 2D integer array triplets,
# where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z]
# that describes the triplet you want to obtain.
# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
# Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5],
# triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

# Time Complexity:
# Space Complexity:

def mergeTriplets(triplets,target):
    flags = [False, False, False]
    match_count = 0

    for x, y, z in triplets:
        if x > target[0] or y > target[1] or z > target[2]:
            continue

        if x == target[0] and not flags[0]:
            flags[0] = True
            match_count += 1

        if y == target[1] and not flags[1]:
            flags[1] = True
            match_count += 1

        if z == target[2] and not flags[2]:
            flags[2] = True
            match_count += 1

        if match_count == 3:
            break

    return match_count == 3