# Problem: House Robber
# Category: Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)

def rob(nums):
    prev, curr = 0, 0

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr
