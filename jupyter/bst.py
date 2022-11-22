
from collections.abc import Iterable
from dspy.node import Node

class BST:
    def __init__(self, keys = None, left = None, right = None):
        if keys is None:
            self.root = None
        else:
            if isinstance(keys, Iterable): 
                self.root = Node(keys[0], left, right)
                for key in keys[1:]:
                    self.add(key) 
            else:
                self.root = Node(keys, left, right)
    
    def delTree(self):
        self.root = None   # garbage collector will do this for us.
        
    def __str__(self):
        return self.root.__str__()
    
    def __iter__(self):
        """iterate through the nodes in the binary tree in level-order"""
        return self.root.__iter__()
        
    def __len__(self):
        if self.root is None: return 0
        return self.root.__len__()
    
    def len(self):
        return self.__len__()
       
    def add(self, key):
        self.root = self._add(self.root, key)
        return self.root is not None

    def _add(self, node, key):
        if node is None:
            node = Node(key)
        else:
            if key < node.key:
                node.left = self._add(node.left, key)
            elif key > node.key:
                node.right = self._add(node.right, key)
            else:
                pass
        return node
    
    def get(self, key):
        return self._get(self.root, key)

    def _get(self, root, key):
        if root is None: return None
    
        if key < root.key:
            return self._get(root.left, key)
        elif key > root.key:
            return self._get(root.right, key)
        else: # found it, return the node
            return root

    def __getitem__(self, key):
        return self.get(key)
    
    def delete(self,key=None):
        if key==None:
            key=self.root.key
        self.root = self._delete(self.root, key)
        return self.root
    
    def _delete(self, node, key):
        if node is None: return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:    #  key == node.key # the node to delete is found
            if node.left and node.right: #two children
                if self._height(node.left)<=self._height(node.right):
                    ikey=self.successor(node).key
                    node.key=ikey
                    node.right=self._delete(node.right,ikey)
                else:
                    ikey=self.predecessor(node).key
                    node.key=ikey
                    node.left=self._delete(node.left,ikey)
                
            elif node.left or node.right: #one child
                node=node.left or node.right
            else: #no child
                node=None
                
        return node
    
    def __delitem__(self,key):
        return self.delete(key)

    #################### your code here #################################
    
    def _height(self,node):
        if node is None:      # base case
            return -1

        left = self._height(node.left)
        right = self._height(node.right)
        return max(left, right) + 1
    
    def height(self):
        return self._height(self.root)
        
    def size(self):
        return self.len()
    
    def __contains__(self, key):
        return bool(self.get(key))
    
    def contains(self, key):
        return self.__contains__(key)

    def _minimum(self,node):
        if node.left==None: return node
        return self._minimum(node.left)
    
    def minimum(self,node=None):
        if node is None: node=self.root
        return self._minimum(node)
    
    def _maximum(self,node):
        if node.right==None: return node
        return self._maximum(node.right)
    
    def maximum(self,node=None):
        if node is None: node=self.root
        return self._maximum(node)
    
    def _predecessor(self,node):
        if node and node.left:
            return self._maximum(node.left)
        
    def predecessor(self,node=None):
        if node is None: node=self.root
        return self._predecessor(node)
    
    def _successor(self,node):
        if node and node.right:
            return self._minimum(node.right)
    
    def successor(self,node=None):
        if node is None: node=self.root
        return self._successor(node)
    
    def isBST(self,node=None):
        if node is None: node=self.root
        return self._isBST(node,float('-inf'), float('inf'))
    
    def _isBST(self,root,min,max):
        if root is None:
            return True
        if min<root.key<max:
            return self._isBST(root.left,min,root.key) and self._isBST(root.right,root.key,max)
        else:
            return False

if __name__ == '__main__':
    print("build 'faith' tree")
    bst = BST('faith')
    print(bst)
    print('length:', len(bst))
    print('height:', bst.height())
    print('  size:', bst.size())

    print('bst contains("a")', bst.contains('a'))             # True
    print('bst contains("b")', bst.contains('b'))             # False

    for x in ['a', 'b']:
        print(f'{x} in bst? ', x in bst)
    print(bst)

    # del 
    print("\ndel bst['f'], bst['i']")
    del bst['f']
    del bst['i']
    print(bst)
    
    print("\ndel all nodes")
    for x in bst:
        del bst[x.key]
    del bst['t']
    print(bst)
    print('length:', bst.len())
    print('height:', bst.height())  
