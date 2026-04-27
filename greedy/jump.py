# Problem: Jump Game
# Category: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [2,3,1,1,4]

max_reach = 0

for i in range(len(nums)):
    if i > max_reach:
        print(False)
        break
    max_reach = max(max_reach, i + nums[i])
else:
    print(True)
