
from src.queue import Queue

class Node(object):
    def __init__(self, val):
        self.val = val
        self.p = None
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def createBalancedTree(self, arr):
        def _create_tree(arr, node, i):
            if i < len(arr):
                tmp = Node(arr[i])
                node = tmp
                node.left = _create_tree(arr, node.left, 2*i+1)
                node.right = _create_tree(arr, node.right, 2*i+2)
            return node
        self.root = _create_tree(arr, self.root, 0)

    def displayTree(self, mode='in-order'):
        if self.root == None:
            print('empty tree')
        else:
            if mode == 'pre-order': self._preorderWalk(self.root)
            if mode == 'post-order': self._postorderWalk(self.root)
            if mode == 'in-order': self._inorderWalk(self.root)
            print('')
    
    def _preorderWalk(self, n):
        if not n is None:
            print(str(n.val), end=' ')
            r = self._preorderWalk(n.left)
            r = self._preorderWalk(n.right)

    def _inorderWalk(self, n):
        if not n is None:
            r = self._inorderWalk(n.left)
            print(str(n.val), end=' ')
            r = self._inorderWalk(n.right)

    def _postorderWalk(self, n):
        if not n is None:
            r = self._postorderWalk(n.left)
            r = self._postorderWalk(n.right)
            print(str(n.val), end=' ')

    def levelorderWalk(self):
        if self.root == None:
            print('empty tree')
        else:
            q = Queue()
            q.enqueue((self.root, 0)) # (node, depth)

            depth_hash = {}
            depth_hash[0] = [(self.root.val, None)] #(node, parent)
            while not q.isempty():
                node_tuple = q.dequeue()
                n = node_tuple[0] # node object
                d = node_tuple[1] # depth value

                if not n.left is None:
                    q.enqueue((n.left, d + 1))
                    if d+1 not in depth_hash:
                        depth_hash[d+1] = [(n.left.val, n.val)]
                    else:
                        depth_hash[d+1].append((n.left.val, n.val))

                if not n.right is None:
                    q.enqueue((n.right, d + 1))
                    if d+1 not in depth_hash:
                        depth_hash[d+1] = [(n.right.val, n.val)]
                    else:
                        depth_hash[d+1].append((n.right.val, n.val))

            for k in depth_hash.keys():
                print('Level '+ str(k) + ': ', end='')
                print(depth_hash[k])

    def isempty(self):
        return True if self.root == None else False
    
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

    def nodecount(self):
        def _count_node(n):
            if n == None:
                return 0
            else:
                left_count = _count_node(n.left)
                right_count = _count_node(n.right)
                return 1 + left_count + right_count
        return _count_node(self.root)

