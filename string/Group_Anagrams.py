# Problem: Group Anagrams
# Category: Hashing
# Time Complexity: O(n*k log k)
# Space Complexity: O(n)

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

groups = defaultdict(list)

for word in strs:
    key = tuple(sorted(word))
    groups[key].append(word)

print(list(groups.values()))
