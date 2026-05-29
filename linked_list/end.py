# Problem: Remove Nth Node From End of List
# Category: Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_nth_from_end(head, n):

    dummy = ListNode(0)
    dummy.next = head

    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
