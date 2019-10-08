class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._next = next
            self._prev = prev
            self._element = element

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, None, None)
        predecessor._next = new_node
        successor._prev = new_node
        new_node._next = successor
        new_node._prev = predecessor
        self._size += 1
        return new_node

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor

        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element