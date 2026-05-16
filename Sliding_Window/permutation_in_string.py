# Problem: Permutation in String
# category: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter

def check_inclusion(s1, s2):
    need = Counter(s1)
    window = Counter()

    left = 0

    for right in range(len(s2)):
        window[s2[right]] += 1

        if right - left + 1 > len(s1):
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

        if window == need:
            return True

    return False
