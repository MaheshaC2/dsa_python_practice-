# Problem: Search Insert Position
# Category: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

nums = [1,3,5,6]
target = 5

low, high = 0, len(nums)-1

while low <= high:
    mid = (low + high)//2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(low)
