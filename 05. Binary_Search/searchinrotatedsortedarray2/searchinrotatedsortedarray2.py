# leetcode 81
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target,
# return true if target is in nums, or false if it is not in nums.

# Time Complexity: O(n)
# Space Complexity: O(1)
def search(nums, target):
    """
        Search for `target` in a rotated sorted list `nums`, which may contain duplicates.
        Returns True if found, False otherwise.
        Time: O(log n) average, O(n) worst-case. Space: O(1).
        """
    left = 0
    right = len(nums) - 1

    # Continue until our search window is empty
    while left <= right:
        mid = (left + right) // 2

        # Check if we found the target
        if nums[mid] == target:
            return True

        # If middle equals left, we can't tell which half is sorted
        # Move left up by one to skip the duplicate
        if nums[mid] == nums[left]:
            left += 1
            continue

        # If the left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target lies within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Otherwise, the right half must be sorted
            # Check if target lies within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    # If we exit the loop, target is not in the list
    return False

print(search([2,5,6,0,0,1,2],0))