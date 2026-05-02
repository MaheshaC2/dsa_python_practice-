#Problem:Reverse linked list
#Category: linked list
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev
