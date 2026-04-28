n = 5
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = dp[i >> 1] + (i & 1)

print(dp)
