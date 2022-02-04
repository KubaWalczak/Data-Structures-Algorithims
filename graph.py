class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addNode(self, node):
        self.numberOfNodes += 1
        graph = self.adjacentList
        graph[node] = []


    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def printgraph(self):
        for k, v in self.adjacentList.items():
            print(f'{k} --> {sorted(v)}')


newGraph = Graph()

newGraph.addNode('0')
newGraph.addNode('1')
newGraph.addNode('2')
newGraph.addNode('3')
newGraph.addNode('4')
newGraph.addNode('5')
newGraph.addNode('6')
newGraph.addEdge('0','1')
newGraph.addEdge('0','2')
newGraph.addEdge('1','3')
newGraph.addEdge('1','2')
newGraph.addEdge('2','4')
newGraph.addEdge('3','4')
newGraph.addEdge('4','5')
newGraph.addEdge('5','6')
newGraph.printgraph()

