# Problem: Fast Exponentiation
# Category: Math
# Time Complexity: O(log n)
# Space Complexity: O(1)

def fast_power(x, n):

    result = 1

    while n > 0:

        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result
