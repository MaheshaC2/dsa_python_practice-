# Problem: Diameter of Binary Tree
# Category: Trees
# Time Complexity: O(n)
# Space Complexity: O(h)

def diameter_of_binary_tree(root):

    diameter = 0

    def dfs(node):

        nonlocal diameter

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    dfs(root)

    return diameter
