# Problem: Course Schedule
# Category: Graph / Topological Sort
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import deque

numCourses = 2
prerequisites = [[1,0]]

graph = {i: [] for i in range(numCourses)}
indegree = [0]*numCourses

for a, b in prerequisites:
    graph[b].append(a)
    indegree[a] += 1

queue = deque([i for i in range(numCourses) if indegree[i] == 0])
count = 0

while queue:
    node = queue.popleft()
    count += 1
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)

print(count == numCourses)
