
from src.binary_search_tree import BinarySearchTree

def testBinarySearchTree():
    '''
    Here we test algorithms for a binary search tree
    We test 
     a) insert in a tree
     b) finding minimum, maximum in a tree
     c) displaying a tree using in-order, pre-order,
        post-order walk, and level-order walk
     d) deleting a node in tree using transplant function
     e) calculating height of a tree
     f) calculating number of nodes in the tree
     g) finding the second largest element
    
    Each node of the binary search tree is an object of
    the Node class, which has a value and the
    left and the right links
    '''

    print('Create an empty tree')
    b = BinarySearchTree()
    print('Display the current tree')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('No. of nodes in the tree: ' + str(b.nodecount()))
    print('Search for 3 in the tree')
    print(b.search(3)[1])
    print('Insert 5')
    b.insert(5)
    print('Current tree height: ' + str(b.treeHeight()))
    print('Second largest element: ' + str(b.secondLargest()))
    print('Insert 3')
    b.insert(3)
    print('Current tree height: ' + str(b.treeHeight()))
    print('Second largest element: ' + str(b.secondLargest()))
    print('Insert 4')
    b.insert(4)
    print('Current tree height: ' + str(b.treeHeight()))
    print('Insert 6')
    b.insert(6)
    print('Current tree height: ' + str(b.treeHeight()))
    print('Insert 5')
    b.insert(5)
    print('Current tree height: ' + str(b.treeHeight()))
    print('Insert 8')
    b.insert(8)
    print('Current tree height: ' + str(b.treeHeight()))
    print('No. of nodes in the tree: ' + str(b.nodecount()))
    print('Second largest element: ' + str(b.secondLargest()))
    print('Is tree empty: ' + str(b.isempty()))
    print('Position of root: ' + str(b.root))
    print('Value of root: ' + str(b.root.val))
    print('Left of root: ' + str(b.root.left.val))
    print('Right of root: ' + str(b.root.right.val))
    print('Tree minimum')
    b.minimum()
    print('Tree maximum')
    b.maximum()
    print('Tree in-order walk')
    b.displayTree()
    print('Tree pre-order walk')
    b.displayTree(mode='pre-order')
    print('Tree post-order walk')
    b.displayTree(mode='post-order')
    print('Tree level-order walk')
    b.levelorderWalk()
    print('Search for 3 in the tree')
    print(b.search(3)[1])
    print('Search for 10 in the list')
    print(b.search(10)[1])
    print('Delete 10 from the tree')
    b.delete(10)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('Delete 8 from the list')
    b.delete(8)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('Delete 4 from the list')
    b.delete(4)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('No. of nodes in the tree: ' + str(b.nodecount()))
    print('Tree level-order walk')
    b.levelorderWalk()
    print('Search for 8 in the list')
    print(b.search(8)[1])
    print('Search for 5 in the list')
    print(b.search(5)[1])
    print('Second largest element: ' + str(b.secondLargest()))
    print('Delete 5 from the list')
    b.delete(5)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('Delete 5 from the list')
    b.delete(5)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('No. of nodes in the tree: ' + str(b.nodecount()))
    print('Tree level-order walk')
    b.levelorderWalk()
    print('Delete 5 from the list')
    b.delete(5)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('No. of nodes in the tree: ' + str(b.nodecount()))
    print('Second largest element: ' + str(b.secondLargest()))
    print('Delete 6 from the list')
    b.delete(6)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('Second largest element: ' + str(b.secondLargest()))
    print('Delete 3 from the list')
    b.delete(3)
    print('Current tree:')
    b.displayTree()
    print('Current tree height: ' + str(b.treeHeight()))
    print('No. of nodes in the tree: ' + str(b.nodecount()))


if __name__ == '__main__':
    print(testBinarySearchTree.__doc__)
    testBinarySearchTree()
