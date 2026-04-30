# Problem: Happy Number
# Category: Math
# Time Complexity: O(log n)
# Space Complexity: O(1)

def get_next(n):
    return sum(int(d)**2 for d in str(n))

n = 19
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    n = get_next(n)

print(n == 1)
