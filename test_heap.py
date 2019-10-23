
from src.heap import MaxHeap
from src.binary_search_tree import BinarySearchTree

def testHeap():
    '''
    Here we test algorithms for a max heap
    The heap class takes a balanced binary tree as
    an input and converts it into a max heap

    We test 
     a) building a max heap
     b) heapify operation
     c) level-order walk
     d) calculating height of a tree
     e) calculating number of nodes in the tree
    
    Each node of the max heap is an object of
    the Node class, which has a value and the
    left and the right links
    '''

    print('Create a binary tree first')
    b = BinarySearchTree()
    b.insert(10)
    b.insert(7)
    b.insert(14)
    b.insert(3)
    b.insert(8)
    b.insert(12)
    b.insert(18)
    print('Tree level-order walk')
    b.levelorderWalk()
    print('Initialize a max heap')
    h = MaxHeap(b.root)
    print('Convert tree to a max heap')
    h.buildMaxHeap(h.root)
    print('Tree level-order walk')
    h.levelorderWalk()
    print('Current tree height: ' + str(h.treeHeight()))
    print('No. of nodes in the tree: ' + str(h.nodecount()))


if __name__ == '__main__':
    print(testHeap.__doc__)
    testHeap()
