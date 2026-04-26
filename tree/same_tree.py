# Problem: Same Tree
# Category: Tree
# Time Complexity: O(n)
# Space Complexity: O(n)

def is_same(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return is_same(p.left, q.left) and is_same(p.right, q.right)
