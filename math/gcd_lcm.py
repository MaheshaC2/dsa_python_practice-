# Problem: GCD & LCM
# Category: Math
# Time Complexity: O(log n)
# Space Complexity: O(1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

print("GCD:", gcd(12, 18))
print("LCM:", lcm(12, 18))
