# leetcode 494
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-'
# before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Time Complexity:
# Space Complexity:

def targetSum(nums,target):
    sum_counts = {0: 1}

    for num in nums:
        next_counts = {}

        for cur_sum, freq in sum_counts.items():
            # add current number
            pos_sum = cur_sum + num
            next_counts[pos_sum] = next_counts.get(pos_sum, 0) + freq

            # subtract current number
            neg_sum = cur_sum - num
            next_counts[neg_sum] = next_counts.get(neg_sum, 0) + freq

        sum_counts = next_counts

    return sum_counts.get(target, 0)