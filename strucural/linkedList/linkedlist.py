class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next


    def showNodes(self):
        for node in self:
            print(node.value)


    def showNodesPretty(self, delimiter = ' -> '):
        nodesToShow = []

        for node in self:
            if node.value is not None:
                nodesToShow.append(node.value)

        print(delimiter.join(nodesToShow))


    def insertAtBegining(self, node):
        node.next = self.head
        self.head = node


    def insertAtEnd(self, node):
        lastNode = self.getLastNode()
        lastNode.next = node


    def insertAfter(self, nodeToFound, nodeToInsert):
        for node in self:
            if (node == nodeToFound):
                if nodeToFound.next is not None:
                    nodeToInsert.next = nodeToFound.next

                nodeToFound.next = nodeToInsert


    def removeNode(self, nodeToRemove):
        lastNode = None

        for currentNode in self:
            if currentNode is nodeToRemove:
                if lastNode:
                    lastNode.next = currentNode.next
                else:
                    self.head = currentNode.next
                
                currentNode.next = None
            else:
                lastNode = currentNode


    def getLastNode(self):
        for node in self:
            if node.next is None:
                return node


    def reverse(self):
        # pointers
        previousNode = Node()
        currentNode = self.head

        while currentNode is not None:
            # keep a ref to the next node
            tempNextNode = currentNode.next

            # reverse
            currentNode.next = previousNode

            # advance prev and cur
            previousNode = currentNode
            currentNode = tempNextNode
        
        self.head = previousNode


# create nodes
FirstNode = Node('First')
SecondNode = Node('Second')
ThirdNode = Node('Third')
JokerNode = Node('Joker')
SecondJokerNode = Node('Second Joker')
LastNode = Node('Last')

# linked nodes
FirstNode.next = SecondNode
SecondNode.next = ThirdNode

# instanciate ll
MyLinkedList = LinkedList()

# set the header
MyLinkedList.head = FirstNode
MyLinkedList.showNodesPretty()

# insert at begin
MyLinkedList.insertAtBegining(JokerNode)
MyLinkedList.showNodesPretty()

# insert at end
MyLinkedList.insertAtEnd(LastNode)
MyLinkedList.showNodesPretty()

# insert after
MyLinkedList.insertAfter(SecondNode, SecondJokerNode)
MyLinkedList.showNodesPretty()

# remove node
# MyLinkedList.removeNode(JokerNode)
# MyLinkedList.removeNode(SecondJokerNode)
# MyLinkedList.showNodesPretty()

# reverse
MyLinkedList.reverse()
MyLinkedList.showNodesPretty()
