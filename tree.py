class Node:
    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            data = current.data
            current = current.left_child
        return data

    def find_max(self):
        current = self.root_node
        while current.right_child:
            data = current.data
            current = current.right_child
        return data

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current.left_child is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current.right_child is None:
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        current = self.root_node
        parent = None
        if current is None:
            return (parent, current)

        while True:
            if current.data == data:
                return (parent, current)
            elif data < current.data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        children_count = 0
        if node.right_child and node.left_child:
            children_count = 2
        elif (node.left_child is None) and node.right_child is None:
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None

            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.right_child is node:
                    parent.right_child = next_node
                else:
                    parent.left_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
