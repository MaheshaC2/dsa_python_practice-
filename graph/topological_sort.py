# Problem: Topological Sort
# Category: Graphs
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import deque

def topological_sort(graph):
    indegree = {u: 0 for u in graph}

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([u for u in indegree if indegree[u] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result
