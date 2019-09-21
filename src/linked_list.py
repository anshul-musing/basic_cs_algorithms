class Node(object):
    def __init__(self, val):
        self.val = val
        self.prv = None
        self.nxt = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert(self, v):
        n = Node(v)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while not curr.nxt == None:
                curr = curr.nxt
            curr.nxt = n
            n.prv = curr
    
    def isempty(self):
        return True if self.head == None else False

    def displayList(self):
        ll = ''
        if not self.head == None:
            curr = self.head
            while not curr.nxt == None:
                ll = ll + str(curr.val) + ' '
                curr = curr.nxt
            else:
                ll = ll + str(curr.val)
        print(ll)
    
    def search(self, x):
        if self.isempty():
            flag = 'list is empty'
            curr = None
        else:
            curr = self.head
            flag = 'not-found'
            while not curr.nxt == None:
                if curr.val == x:
                    flag = 'found'
                    break
                curr = curr.nxt
            else:
                if curr.val == x:
                    flag = 'found'
        return curr, flag
    
    def delete(self, v):
        if self.isempty():
            print('list is empty')
        else:
            c,f = self.search(v)
            if f == 'not-found':
                print('requested deletion doesn\'t exist')
            else:
                if c.prv == None: #it's the first node
                    if not c.nxt == None:
                        c.nxt.prv = c.prv
                    else:
                        self.head = None
                else:
                    c.prv.nxt = c.nxt
                    if not c.nxt == None: c.nxt.prv = c.prv
                del c
