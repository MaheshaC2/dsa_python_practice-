# Problem: Move Zeros
# Category: Array
# Approach: Filter non-zero elements and append zeros
# Time Complexity: O(n)
# Space Complexity: O(n)

nums = [0,1,0,3,12]

result = [x for x in nums if x != 0]
result += [0] * (len(nums) - len(result))

print(result)
