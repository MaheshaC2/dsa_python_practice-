# Problem: Clone Graph
# Category: Graphs
# Time Complexity: O(V + E)
# Space Complexity: O(V)

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):

    old_to_new = {}

    def dfs(node):

        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node) if node else None
