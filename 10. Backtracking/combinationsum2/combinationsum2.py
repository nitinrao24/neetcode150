# leetcode 40
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

# Time Complexity:
# Space Complexity:

def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def dfs(remaining_target, start, comb):
        if remaining_target < 0:
            return
        if remaining_target == 0:
            res.append(comb)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining_target:
                break
            dfs(remaining_target - candidates[i], i + 1, comb + [candidates[i]])

    dfs(target, 0, [])
    return res

print(combinationSum2([10,1,2,7,6,1,5], 8))