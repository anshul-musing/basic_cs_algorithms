
from src.stack import Stack

def testStack():
    '''
    Here we test algorithms for stacks
    We test pushing, popping, and checking if 
    a stack is empty

    Stack is implemented as a python list
    It's not the best implementation as we'll
    show that the stack will be empty yet it 
    will be occupying memory with the previously 
    inserted elements
    '''

    print('Create an empty stack')
    s = Stack()
    print('Pop now')
    print('Topmost element: ' + str(s.pop()))
    print('Insert 5')
    s.push(5)
    print('Insert 3')
    s.push(3)
    print('Insert 4')
    s.push(4)
    print('Is stack empty: ' + str(s.isempty()))
    print('Position of top: ' + str(s.top))
    print('Pop now')
    print('Topmost element: ' + str(s.pop()))
    print('Pop now')
    print('Topmost element: ' + str(s.pop()))
    print('Pop now')
    print('Topmost element: ' + str(s.pop()))
    print('Pop now')
    print('Topmost element: ' + str(s.pop()))
    print('Stack in the memory')
    print(s.storage)


if __name__ == '__main__':
    print(testStack.__doc__)
    testStack()
