#Problem: Check if Graph is Bipartite
#Category: Graphs
#Time Complexity: O(V + E)
#Space Complexity: O(V)


def is_bipartite(graph):

    color = {}

    for node in range(len(graph)):

        if node not in color:

            stack = [node]
            color[node] = 0

            while stack:

                current = stack.pop()

                for neighbor in graph[current]:

                    if neighbor not in color:

                        color[neighbor] = 1 - color[current]
                        stack.append(neighbor)

                    elif color[neighbor] == color[current]:
                        return False

    return True
