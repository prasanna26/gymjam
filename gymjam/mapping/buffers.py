from collections import deque

class EmptyBuffer:

    def is_overpopulated(self):
        return False

    def add_individual(self, to_add):
        pass

    def remove_individual(self):
        return None

class SlidingBuffer:

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer_queue = deque(maxlen=buffer_size+1)

    def is_overpopulated(self):
        return len(self.buffer_queue) > self.buffer_size

    def add_individual(self, to_add):
        self.buffer_queue.append(to_add)

    def remove_individual(self):
        return self.buffer_queue.popleft()
