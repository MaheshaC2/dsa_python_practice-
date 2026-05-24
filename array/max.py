# Problem: Maximum Product Subarray
# Category: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_product(nums):
    current_max = current_min = result = nums[0]

    for num in nums[1:]:

        temp = current_max * num

        current_max = max(num, temp, current_min * num)
        current_min = min(num, temp, current_min * num)

        result = max(result, current_max)

    return result
