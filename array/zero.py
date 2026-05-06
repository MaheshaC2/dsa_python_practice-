# Problem: Move All Zeros to End
# Category: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums
