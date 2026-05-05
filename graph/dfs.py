# Problem: Depth First Search (DFS)
# Category: Graphs
# Time Complexity: O(V + E)
# Space Complexity: O(V)


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
