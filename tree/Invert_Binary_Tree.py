# Problem: Invert Binary Tree
# Category: Tree
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def invert(root):
    if not root:
        return None

    root.left, root.right = invert(root.right), invert(root.left)
    return root
