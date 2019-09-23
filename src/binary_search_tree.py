class Node(object):
    def __init__(self, val):
        self.val = val
        self.p = None
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.tree = ''
    
    def insert(self, v):
        n = Node(v)
        if self.root == None:
            self.root = n
        else:
            x = self.root
            while not x == None:
                y = x
                x = x.left if v < x.val else x.right
            n.p = y
            if v < y.val: y.left = n
            if v >= y.val: y.right = n
    
    def displayTree(self, mode='in-order'):
        if self.root == None:
            print('empty tree')
        else:
            self.tree = ''
            if mode == 'pre-order':
                self._preorderWalk(self.root)
            elif mode == 'post-order':
                self._postorderWalk(self.root)
            else:
                self._inorderWalk(self.root)
            print(self.tree)
    
    def _preorderWalk(self, n):
        if not n is None:
            self.tree = self.tree + str(n.val) + ' '
            r = self._preorderWalk(n.left)
            r = self._preorderWalk(n.right)

    def _inorderWalk(self, n):
        if not n is None:
            r = self._inorderWalk(n.left)
            self.tree = self.tree + str(n.val) + ' '
            r = self._inorderWalk(n.right)

    def _postorderWalk(self, n):
        if not n is None:
            r = self._postorderWalk(n.left)
            r = self._postorderWalk(n.right)
            self.tree = self.tree + str(n.val) + ' '
    
    def search(self, i):
        if self.root == None:
            flag = 'empty tree'
            x = None
        else:
            x = self.root
            flag = 'not-found'
            while not x is None:
                if x.val == i:
                    flag = 'found'
                    break
                else:
                    if i < x.val: x = x.left
                    if i > x.val: x = x.right
        return x, flag
    
    def minimum(self):
        if self.root == None:
            print('empty tree')
        else:
            x = self.root
            while not x.left is None: x = x.left
            print(x.val)

    def maximum(self):
        if self.root == None:
            print('empty tree')
        else:
            x = self.root
            while not x.right is None: x = x.right
            print(x.val)

    def isempty(self):
        return True if self.root == None else False
    
    def _transplant(self, u, v):
        if u.p == None: #it's a root node
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if not v == None: v.p = u.p
    
    def _minsubtree(self, x):
        while not x.left == None: x = x.left
        return x

    def _maxsubtree(self, x):
        while not x.right == None: x = x.right
        return x
    
    def delete(self, v):
        if self.root == None:
            print('empty tree')
        else:
            c,f = self.search(v)
            if f == 'not-found':
                print('requested deletion doesn\'t exist')
            else:
                if c.left == None:
                    self._transplant(c, c.right)
                elif c.right == None:
                    self._transplant(c, c.left)
                else:
                    y = self._minsubtree(c.right)
                    if not y.p == c:
                        self._transplant(y, y.right)
                        y.right = c.right
                        y.right.p = y
                    self._transplant(c, y)
                    y.left = c.left
                    y.left.p = y
                del c

    def treeHeight(self):
        def _treeHeight(n):
            if n == None:
                return 0
            else:
                left_ht = _treeHeight(n.left)
                right_ht = _treeHeight(n.right)
                if left_ht > right_ht:
                    return left_ht+1
                else:
                    return right_ht+1
        return _treeHeight(self.root)

    def secondLargest(self):
        if (self.root == None) or \
            (self.root.left == None and self.root.right == None):
            return 'error :: tree does not have at least two nodes'
        else:
            x = self.root
            while not x == None:
                if (not x.right == None) and \
                    (x.right.left == None) and \
                    (x.right.right == None):
                    return x.val

                if (x.right == None) and \
                    (not x.left == None):
                    y = self._maxsubtree(x.left)
                    return y.val

                x = x.right

