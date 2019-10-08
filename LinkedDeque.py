from ._DoublyLinkedBase import _DoublyLinkedBase

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise ValueError('The Dequeue is empty')
        return self._head._next._element

    def last(self):
        if self.is_empty():
            raise ValueError('The Dequeue is empty')
        return self._tail._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._head, self._head._next)

    def insert_last(self, e):
        self._insert_between(e, self._tail._prev, self._tail)

    def delete_first(self):
        if self.is_empty():
            raise ValueError('The Dequeue is empty')
        self._delete_node(self._head._next)

    def delete_last(self):
        if self.is_empty():
            raise ValueError('The Dequeue is empty')
        self._delete_node(self._tail._prev)