
from src.heap import MaxHeap

def testHeap():
    '''
    Here we test algorithms for a max heap
    The heap class takes a balanced binary tree as
    an input and converts it into a max heap

    We test 
     a) building a max heap
     b) heapify operation
    
    Each node of the max heap is an object of
    the Node class, which has a value and the
    left and the right links
    '''

    print('Initialize a max heap')
    h = MaxHeap()
    print('Create a binary tree first')
    elem = [10,7,14,3,8,12,18,20,19,1,2]
    h.createBalancedTree(elem)
    print('Tree level-order walk')
    h.levelorderWalk()
    print('Convert tree to a max heap')
    h.buildMaxHeap(h.root)
    print('Tree level-order walk')
    h.levelorderWalk()
    print('Current tree height: ' + str(h.treeHeight()))
    print('No. of nodes in the tree: ' + str(h.nodecount()))


if __name__ == '__main__':
    print(testHeap.__doc__)
    testHeap()
