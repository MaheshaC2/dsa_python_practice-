# Problem: Container With Most Water
# Category: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

height = [1,8,6,2,5,4,8,3,7]

l, r = 0, len(height)-1
max_area = 0

while l < r:
    area = min(height[l], height[r]) * (r - l)
    max_area = max(max_area, area)

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(max_area)
