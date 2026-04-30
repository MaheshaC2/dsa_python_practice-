# Problem: 0/1 Knapsack
# Category: Dynamic Programming
# Time Complexity: O(n*w)
# Space Complexity: O(w)

weights = [1,2,3]
values = [6,10,12]
capacity = 5

dp = [0]*(capacity+1)

for i in range(len(weights)):
    for w in range(capacity, weights[i]-1, -1):
        dp[w] = max(dp[w], values[i] + dp[w-weights[i]])

print("Max value:", dp[capacity])
