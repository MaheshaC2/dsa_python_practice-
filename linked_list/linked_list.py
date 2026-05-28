# Problem: Intersection of Two Linked Lists
# Category: Linked List
# Time Complexity: O(n + m)
# Space Complexity: O(1)

def get_intersection_node(headA, headB):

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a
