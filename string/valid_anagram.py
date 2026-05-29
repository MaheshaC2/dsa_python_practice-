# Problem: Valid Anagram
# Category: Strings
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
