# Problem: Moving Average from Data Stream
# Category: Queue
# Time Complexity: O(1)
# Space Complexity: O(n)

from collections import deque
class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val):

        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()

        return self.total / len(self.queue)
