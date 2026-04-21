# Problem: Reverse Words in a String
# Category: String
# Approach: Split and reverse
# Time Complexity: O(n)
# Space Complexity: O(n)

s = "hello world"

result = " ".join(s.split()[::-1])

print("Input:", s)
print("Output:", result)
