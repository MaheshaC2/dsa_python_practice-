"""
Problem: Sieve of Eratosthenes
Category: Math
Time Complexity: O(n log log n)
Space Complexity: O(n)
"""

def sieve(n):
    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [i for i in range(2, n + 1) if prime[i]]
