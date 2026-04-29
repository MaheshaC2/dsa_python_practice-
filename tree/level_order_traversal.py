# Problem: Level Order Traversal
# Category: Tree / BFS
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

queue = deque([root])

while queue:
    node = queue.popleft()
    print(node.val, end=" ")

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
