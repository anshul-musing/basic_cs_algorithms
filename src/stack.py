class Stack(object):
    def __init__(self):
        self.storage = []
        self.top = -1
    
    def push(self, val):
        self.storage.append(val)
        self.top += 1
    
    def isempty(self):
        return False if self.top >= 0 else True
    
    def pop(self):
        if not self.isempty():
            val = self.storage[self.top]
            self.top -= 1
            return val
        else:
            return 'stack is empty'
