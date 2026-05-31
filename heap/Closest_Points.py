# Problem: K Closest Points to Origin
# Category: Heap
# Time Complexity: O(n log k)
# Space Complexity: O(k)

import heapq

def k_closest(points, k):

    heap = []

    for x, y in points:

        distance = -(x * x + y * y)

        if len(heap) < k:
            heapq.heappush(heap, (distance, [x, y]))

        elif distance > heap[0][0]:
            heapq.heapreplace(heap, (distance, [x, y]))

    return [point for _, point in heap]
