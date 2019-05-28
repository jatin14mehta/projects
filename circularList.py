class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node

        self.head.next = self.tail
        self.count += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail

        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.count -= 1
                return

            prev = current
            current = current.next
