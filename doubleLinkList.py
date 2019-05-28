class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False
