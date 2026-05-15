"""
Problem: Group Anagrams
Category: Hashing
Time Complexity: O(n * k log k)
Space Complexity: O(n)
"""

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
