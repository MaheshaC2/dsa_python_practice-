# Problem: Longest Palindromic Substring
# Category: Strings
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def longest_palindrome(s):

    result = ""

    for i in range(len(s)):

        left = right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:

            if len(s[left:right + 1]) > len(result):
                result = s[left:right + 1]

            left -= 1
            right += 1

        left, right = i, i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:

            if len(s[left:right + 1]) > len(result):
                result = s[left:right + 1]

            left -= 1
            right += 1

    return result
