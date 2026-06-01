"""
Problem: Number of Connected Components
Category: Union Find
Time Complexity: O(E * α(n))
Space Complexity: O(n)
"""

def count_components(n, edges):

    parent = list(range(n))

    def find(x):

        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x

    def union(x, y):

        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return 0

        parent[root_x] = root_y

        return 1

    components = n

    for u, v in edges:
        components -= union(u, v)

    return components
