class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def addFirst(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def addLast(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index):
        self._validate_index(index)
        return self._node_at(index).value

    def removeFirst(self):
        if self.head is None:
            raise IndexError("removeFirst from empty list")

        removed = self.head
        self.head = removed.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return removed.value

    def remove(self, index):
        self._validate_index(index)

        if index == 0:
            return self.removeFirst()

        prev = self._node_at(index - 1)
        removed = prev.next
        prev.next = removed.next

        if removed is self.tail:
            self.tail = prev

        self._size -= 1
        return removed.value

    def removeLast(self):
        if self.head is None:
            raise IndexError("removeLast from empty list")

        if self.head is self.tail:
            value = self.head.value
            self.clear()
            return value

        prev = self.head
        while prev.next is not self.tail:
            prev = prev.next

        value = self.tail.value
        prev.next = None
        self.tail = prev
        self._size -= 1
        return value

    def size(self):
        return self._size

    def add(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")

        if index == 0:
            self.addFirst(value)
            return

        if index == self._size:
            self.addLast(value)
            return

        prev = self._node_at(index - 1)
        prev.next = Node(value, prev.next)
        self._size += 1

    def _node_at(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def _validate_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
