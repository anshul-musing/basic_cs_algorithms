
from src.binary_tree import Node
from src.binary_tree import BinaryTree

class MaxHeap(BinaryTree):
    def __init__(self):
        super().__init__()

    def buildMaxHeap(self, node):
        if not node is None:
            self.buildMaxHeap(node.left)
            self.buildMaxHeap(node.right)
            self.heapify(node)

    def heapify(self, node):
        maxNode = node
        if node.left is not None and node.left.val > maxNode.val:
            maxNode = node.left
        if node.right is not None and node.right.val > maxNode.val:
            maxNode = node.right

        if not maxNode == node:
            self.swapNodeValues(node, maxNode)
            self.heapify(maxNode)

    def swapNodeValues(self, n1, n2):
        tmp = n1.val
        n1.val = n2.val
        n2.val = tmp
