from src.queue import Queue

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MaxHeap(object):
    def __init__(self, node=None):
        self.root = node

    def buildMaxHeap(self, node):
        if not node is None:
            self.buildMaxHeap(node.left)
            self.buildMaxHeap(node.right)
            self.heapify(node)

    def heapify(self, node):
        maxNode = node
        if node.left is not None and node.left.val > maxNode.val:
            maxNode = node.left
        if node.right is not None and node.right.val > maxNode.val:
            maxNode = node.right

        if not maxNode == node:
            self.swapNodeValues(node, maxNode)
            self.heapify(maxNode)

    def swapNodeValues(self, n1, n2):
        tmp = n1.val
        n1.val = n2.val
        n2.val = tmp

    def levelorderWalk(self):
        if self.root == None:
            print('empty tree')
        else:
            q = Queue()
            q.enqueue((self.root, 1)) # (node, depth)

            depth_hash = {}
            depth_hash[1] = [str(self.root.val)]
            while not q.isempty():
                node_tuple = q.dequeue()
                n = node_tuple[0]
                d = node_tuple[1]

                if not n.left is None:
                    q.enqueue((n.left, d + 1))
                    if d+1 not in depth_hash:
                        depth_hash[d+1] = [str(n.left.val)]
                    else:
                        depth_hash[d+1].append(str(n.left.val))

                if not n.right is None:
                    q.enqueue((n.right, d + 1))
                    if d+1 not in depth_hash:
                        depth_hash[d+1] = [str(n.right.val)]
                    else:
                        depth_hash[d+1].append(str(n.right.val))

            for k in depth_hash.keys():
                print('Level '+ str(k) + ': ' + ', '.join(depth_hash[k]))

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

