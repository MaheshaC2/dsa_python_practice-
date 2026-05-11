# Problem: Factorial Using Recursion
# Category: Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
