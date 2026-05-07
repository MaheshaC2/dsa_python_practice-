# Problem: Find Middle of Linked List
# Category: Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)

def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
