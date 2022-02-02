

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None



class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def enqueue(self,data):

        new_item = Node(data)

        if self.first == None:
            self.first = new_item
            self.last = new_item
        else:
            self.last.next = new_item
            self.last = new_item

    def dequeue(self):
        if self.first == None:
            return print("empty queue")
        else:
            deleting = self.first
            self.first = self.first.next
            del(deleting)



    def printe(self):
        queue = []
        current = self.first

        while current!= None:
            if current == self.first:
                queue.append(f"[First {current.data}]")
            elif current.next == None:
                queue.append(f"[Last {current.data}]")
            else:
                queue.append(f"[{current.data}]")
            current = current.next
        return print('-> '.join(queue))

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.printe()
q1.dequeue()
q1.printe()
