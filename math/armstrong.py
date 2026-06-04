"""
Problem: Armstrong Number
Category: Math
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def is_armstrong(n):

    digits = len(str(n))

    total = sum(
        int(digit) ** digits
        for digit in str(n)
    )

    return total == n
