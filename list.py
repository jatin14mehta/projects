class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


n1 = Node("egg")
n2 = Node("ham")
n3 = Node('sam')
n4 = Node({'name': 'jatin', 'age': 25})
n1.next = n2
n2.next = n3
n3.next = n4
print(n2.next)

current = n1
while current:
    print(current.data)
    current = current.next


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(self)
        self.size += 1
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
