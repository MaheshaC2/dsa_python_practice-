# Problem: Breadth First Search (BFS)
# Category: Graphs
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
