
from src.linked_list import LinkedList

def testLinkedList():
    '''
    Here we test algorithms for linked lists
    We test insert, delete, and search functions
    Each node of the linked list is an object of
    the Node class, which has a value and the
    previous and the next links
    '''

    print('Create an empty linked list')
    l = LinkedList()
    print('Display the current list')
    l.displayList()
    print('Search for 3 in the list')
    print(l.search(3)[1])
    print('Insert 5')
    l.insert(5)
    print('Insert 3')
    l.insert(3)
    print('Insert 4')
    l.insert(4)
    print('Is list empty: ' + str(l.isempty()))
    print('Position of head: ' + str(l.head))
    print('Value of head: ' + str(l.head.val))
    print('Next of head: ' + str(l.head.nxt.val))
    print('Display the current list')
    l.displayList()
    print('Search for 3 in the list')
    print(l.search(3)[1])
    print('Search for 10 in the list')
    print(l.search(10)[1])
    print('Delete 10 from the list')
    l.delete(10)
    print('Current list:')
    l.displayList()
    print('Delete 3 from the list')
    l.delete(3)
    print('Current list:')
    l.displayList()
    print('Delete 4 from the list')
    l.delete(4)
    print('Current list:')
    l.displayList()
    print('Search for 3 in the list')
    print(l.search(3)[1])
    print('Search for 5 in the list')
    print(l.search(5)[1])
    print('Delete 5 from the list')
    l.delete(5)
    print('Current list:')
    l.displayList()
    print('Insert 6')
    l.insert(6)
    print('Display the current list')
    l.displayList()
    print('Delete 6 from the list')
    l.delete(6)
    print('Current list:')
    l.displayList()
    print('Delete 6 from the list')
    l.delete(6)
    print('Current list:')
    l.displayList()


if __name__ == '__main__':
    print(testLinkedList.__doc__)
    testLinkedList()
