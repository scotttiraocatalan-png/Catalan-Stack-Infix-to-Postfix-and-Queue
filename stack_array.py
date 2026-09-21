"""ITECC04 Laboratory 4, Part A1: the array-based stack.

Fill in one step at a time. Run test_stack.py after every step.

The list is the storage, and the END of the list is the top. That single
decision is what makes push and pop cost O(1): appending and popping at the
end of a Python list does not move any other element. Choosing index 0 as the
top would make every operation shift the whole list.

Nothing outside this class may touch self._items. That is the encapsulation
the rubric marks.
"""


class ArrayStack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __len__(self):
        return self.size()