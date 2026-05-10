"""
Problem: Generate All Subsets
Category: Backtracking
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
