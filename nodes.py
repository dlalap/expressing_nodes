class Node:
    def __init__(self, id=None):
        self.id = id
        self.nextNode = None


if __name__ == '__main__':
    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")

    n1.nextNode = n2
    n2.nextNode = n3

    currentNode = n1
    while currentNode:
        print(currentNode.id)
        currentNode = currentNode.nextNode

    print('End of program.')
