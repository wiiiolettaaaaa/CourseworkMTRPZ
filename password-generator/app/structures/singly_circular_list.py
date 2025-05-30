class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        if not self.tail:
            return []
        result = []
        current = self.tail.next
        while True:
            result.append(current.data)
            if current == self.tail:
                break
            current = current.next
        return result