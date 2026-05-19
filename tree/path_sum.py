# Problem: Path Sum
# Category: Trees
# Time Complexity: O(n)
# Space Complexity: O(h)


def has_path_sum(root, target_sum):

    if not root:
        return False

    if not root.left and not root.right:
        return target_sum == root.val

    target_sum -= root.val

    return (
        has_path_sum(root.left, target_sum) or
        has_path_sum(root.right, target_sum)
    )
