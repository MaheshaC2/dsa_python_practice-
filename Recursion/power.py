# Problem: Power (x^n)
# Category: Recursion
# Time Complexity: O(log n)
# Space Complexity: O(log n)

def power(x, n):
    if n == 0:
        return 1
    half = power(x, n//2)
    if n % 2 == 0:
        return half * half
    return x * half * half

print(power(2, 10))
