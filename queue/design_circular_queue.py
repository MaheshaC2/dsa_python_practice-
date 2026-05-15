# Problem: Design Circular Queue
# Category: Queue
# Time Complexity: O(1)
# Space Complexity: O(k)

class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.size = k

    def enQueue(self, value):
        if self.isFull():
            return False

        tail = (self.head + self.count) % self.size
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self):
        tail = (self.head + self.count - 1) % self.size
        return -1 if self.isEmpty() else self.queue[tail]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
