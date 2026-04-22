# Problem: Rotate Array by K steps
# Category: Array
# Approach: Reverse method

def rotate(nums, k):
    k = k % len(nums)

    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Example
nums = [1,2,3,4,5]
k = 2

print("Input:", nums)
print("Output:", rotate(nums, k))
