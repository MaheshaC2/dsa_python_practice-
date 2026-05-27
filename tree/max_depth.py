# Problem: Maximum Depth of Binary Tree
# Category: Trees
# Time Complexity: O(n)
# Space Complexity: O(h)

def max_depth(root):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))
