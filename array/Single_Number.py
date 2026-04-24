# Problem: Single Number
# Category: Bit Manipulation
# Approach: XOR cancels duplicates
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [4,1,2,1,2]

result = 0
for num in nums:
    result ^= num

print("Single Number:", result)
