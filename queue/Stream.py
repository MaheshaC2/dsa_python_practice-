# Problem: First Unique Character in Stream
# Category: Queue
# Time Complexity: O(1)
# Space Complexity: O(n)


from collections import deque

class FirstUnique:

    def __init__(self):
        self.queue = deque()
        self.count = {}

    def add(self, value):

        self.count[value] = self.count.get(value, 0) + 1
        self.queue.append(value)

        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()

    def first_unique(self):
        return self.queue[0] if self.queue else -1
