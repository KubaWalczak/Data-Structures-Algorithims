
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0

    def add(self,data):
        new_element = Node(data)
        new_element.next = self.top
        self.top = new_element

    def pop(self):
        if self.top:
            current_top = self.top
            self.top = current_top.next
            del(current_top)
        else:
            return print('empty stack - nothing to delete')

    def peek(self):
        return print(self.top.data)

    def is_empty(self):
        lenght = self.lenght
        current = self.top
        if current:
            while current:
                lenght += 1
                current = current.next

            return lenght
        else:
            return print('empty stack')

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.top



        while current:
            if current is self.top:
                nodes.append(f"[TOP: {current.data}]")
            elif current.next is None:
                nodes.append(f"[BOTTOM: {current.data}]")
            else:
                nodes.append(f" {current.data}")
            current = current.next
        return '-> '.join(nodes)

a = Stack()

a.add(10)
a.add(20)
print(a)
a.peek()


