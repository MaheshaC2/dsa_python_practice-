# Problem: Find Missing Number (0 to n)
# Category: Array / Math
# Approach: Use sum formula
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [3,0,1]

n = len(nums)
expected = n * (n + 1) // 2
actual = sum(nums)

print("Missing:", expected - actual)
