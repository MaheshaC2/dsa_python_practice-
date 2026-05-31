# Problem: Merge K Sorted Lists
# Category: Heap
# Time Complexity: O(N log K)
# Space Complexity: O(K)

import heapq

def merge_k_lists(lists):

    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:

        value, i, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(
                heap,
                (node.next.val, i, node.next)
            )

    return dummy.next
