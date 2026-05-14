# Problem: Contains Duplicate
# Category: Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)


def contains_duplicate(nums):
    return len(nums) != len(set(nums))
