"""
Problem: Partition Equal Subset Sum
Category: Dynamic Programming
Time Complexity: O(n * sum)
Space Complexity: O(sum)
"""

def can_partition(nums):

    total = sum(nums)

    if total % 2:
        return False

    target = total // 2

    dp = set([0])

    for num in nums:

        next_dp = dp.copy()

        for t in dp:
            if t + num == target:
                return True

            next_dp.add(t + num)

        dp = next_dp

    return target in dp
