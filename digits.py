"""
Problem: Count Number of Digits
Category: Math
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def count_digits(n):

    count = 0

    while n:
        count += 1
        n //= 10

    return count
