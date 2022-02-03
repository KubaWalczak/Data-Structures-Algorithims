
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_data = Node(data)

        if self.root is None:
            self.root = new_data
            return self.root.data
        else:
            currentNode = self.root
            while True:
                #right
                if new_data.data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = new_data
                        return self
                    currentNode = currentNode.right

                #left
                elif new_data.data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = new_data
                        return self
                    currentNode = currentNode.left
                else:
                    return print('no duplicates allowed')


    def search(self,data):
        value = Node(data)
        # current = self.root

        if self.root is None:
            return 'empty tree'
        else:
            current = self.root
            try:
                while True:
                    #root
                    if value.data == current.data:
                        return True, current.data
                    #right
                    elif value.data > current.data:
                        if value.data == current.right.data:
                            return True, current.right.data
                        current = current.right
                    #left
                    else:
                        if value.data == current.right.data:
                            return True, current.right.data
                        current = current.left
            except AttributeError:
                return False, 'brak wyników'







a = BinarySearchTree()

a.insert(10)
a.insert(12)
a.insert(14)
a.insert(6)
a.insert(8)
print(a.search(6))