class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError('The Queue is empty')
        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise ValueError('The Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, element):
        newtail = self._Node(element, None)
        if self.is_empty():
            newtail._next = newtail
        else:
            newtail._next = self._tail._next
            self._tail._next = newtail
        self._tail = newtail
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
