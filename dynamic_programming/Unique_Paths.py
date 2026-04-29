# Problem: Unique Paths
# Category: Dynamic Programming
# Time Complexity: O(m*n)
# Space Complexity: O(n)

m, n = 3, 3

dp = [1] * n

for _ in range(m-1):
    for j in range(1, n):
        dp[j] += dp[j-1]

print(dp[-1])
