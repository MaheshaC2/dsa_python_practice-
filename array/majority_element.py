# Problem: Majority Element
# Category: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num == candidate else -1

    return candidate
