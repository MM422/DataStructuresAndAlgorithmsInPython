class LinkedStack:
    class _Node:
        __slots__ = '_element', 'next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return false

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        poped_element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return poped_element