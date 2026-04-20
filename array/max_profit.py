# Problem: Best Time to Buy and Sell Stock
# Category: Array
# Approach: Track minimum price
# Time Complexity: O(n)
# Space Complexity: O(1)

prices = [7,1,5,3,6,4]

min_price = float('inf')
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

print("Max Profit:", max_profit)
