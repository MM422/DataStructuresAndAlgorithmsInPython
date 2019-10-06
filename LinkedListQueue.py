class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = None

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def first(self):
        if self.is_empty():
            raise ValueError('The Queue is empty')
        return self._head._element

    def enqueue(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('The Queue is empty')
        dequeued_item = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return dequeued_item
