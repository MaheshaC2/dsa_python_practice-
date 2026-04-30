# Problem: Next Greater Element
# Category: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

nums = [2,1,2,4,3]
res = [-1]*len(nums)
stack = []

for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        res[idx] = nums[i]
    stack.append(i)

print(res)
