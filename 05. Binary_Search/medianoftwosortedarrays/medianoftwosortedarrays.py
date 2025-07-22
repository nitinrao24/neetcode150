# leetcode 4
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Time Complexity:
# Space Complexity:

def medianoftwosortedarrays(arr1,arr2):
    if len(arr1) > len(arr2):
        return self.findMedianSortedArrays(arr2, arr1)
    n1 = len(arr1)
    n2 = len(arr2)
    low = 0
    high = n1
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (n1 + n2 + 1) // 2 - cut1
        left_max_1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
        right_min_1 = float('inf') if cut1 == n1 else arr1[cut1]
        left_max_2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
        right_min_2 = float('inf') if cut2 == n2 else arr2[cut2]
        if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
            if (n1 + n2) % 2 == 0:
                return (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2
            return max(left_max_1, left_max_2)
        if left_max_1 > right_min_2:
            high = cut1 - 1
        else:
            low = cut1 + 1

print(medianoftwosortedarrays([1,2],[3,4]))