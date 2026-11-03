class InMemoryQueue:
    """Custom FIFO Queue using array manipulation."""
    def __init__(self):
        self._items = []
        self._head = 0

    def enqueue_batch(self, batch):
        for item in batch:
            self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self._items[self._head]
        self._items[self._head] = None 
        self._head += 1
        if self._head > 1000:
            self._items = self._items[self._head:]
            self._head = 0
        return item

    def is_empty(self):
        return self._head >= len(self._items)

    def size(self):
        return len(self._items) - self._head