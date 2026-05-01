# Problem: Non-overlapping Intervals
# Category: Greedy
# Time Complexity: O(n log n)
# Space Complexity: O(1)

intervals = [[1,2],[2,3],[3,4],[1,3]]

intervals.sort(key=lambda x: x[1])
count = 0
end = intervals[0][1]

for i in range(1, len(intervals)):
    if intervals[i][0] < end:
        count += 1
    else:
        end = intervals[i][1]

print("Remove:", count)
