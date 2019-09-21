
from src.queue import Queue

def testQueue():
    '''
    Here we test algorithms for queues
    We test enqueue, dequeue, and checking if 
    a queue is empty

    Queue is implemented as a python list
    It's not the best implementation as we'll
    show that the queue will be empty yet it 
    will be occupying memory with the previously 
    inserted elements
    '''

    print('Create an empty queue')
    q = Queue()
    print('Dequeue now')
    print('Dequeued element: ' + str(q.dequeue()))
    print('Insert 5')
    q.enqueue(5)
    print('Insert 3')
    q.enqueue(3)
    print('Insert 4')
    q.enqueue(4)
    print('Is queue empty: ' + str(q.isempty()))
    print('Position of head: ' + str(q.head))
    print('Position of tail: ' + str(q.tail))
    print('Dequeue now')
    print('Dequeued element: ' + str(q.dequeue()))
    print('Dequeue now')
    print('Dequeued element: ' + str(q.dequeue()))
    print('Dequeue now')
    print('Dequeued element: ' + str(q.dequeue()))
    print('Dequeue now')
    print('Dequeued element: ' + str(q.dequeue()))
    print('Queue in the memory')
    print(q.storage)
    print('Insert 6')
    q.enqueue(6)
    print('Dequeue now')
    print('Dequeued element: ' + str(q.dequeue()))
    print('Queue in the memory')
    print(q.storage)
    

if __name__ == '__main__':
    print(testQueue.__doc__)
    testQueue()
