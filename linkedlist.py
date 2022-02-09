
class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"Node data: {self.data}"


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = self.head


    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count

    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def append(self,data):
        new_node = Node(data)
        last_node = Node(data)
        if self.head == None:
            self.head = last_node
            self.tail = self.head
        else:
            self.tail.next_node = last_node
            self.tail = last_node

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding node at insertion point takes
        O(n) time.
        Takes overall O(n) time.
        """


        if index == 0:
            self.add(data)
            return
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node





    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None


l1 = LinkedList()

l1.add(15)
l1.add(13)
l1.add(12)
print(l1)

l1.insert(15,3)
print(l1)
l1.append(11)