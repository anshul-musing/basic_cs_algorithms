class Queue(object):
    def __init__(self):
        self.storage = []
        self.head = 0
        self.tail = -1
    
    def enqueue(self, val):
        self.storage.append(val)
        self.tail += 1
    
    def isempty(self):
        return False if self.head <= self.tail else True
    
    def dequeue(self):
        if not self.isempty():
            val = self.storage[self.head]
            self.head += 1
            return val
        else:
            return 'queue is empty'
