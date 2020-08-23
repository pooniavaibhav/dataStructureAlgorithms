class TreeEmptyError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self,x):
        self.root = self._insert(self.root, x)

    def _insert(self,p,x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild, x)
        else:
            print(x, "already present in the tree")
        return p

    def search(self,x):
        return self._search(self.root, x) is not None

    def _search(self, p, x):
        if p is None:
            return None #key not found
        if x < p.info: # search in left sub tree
            return self._search(p.lchild, x)
        if x > p.info: #search in right sub tree
            return self._search(p.rchild, x)
        return p

    def search1(self,x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild #move to left child
            elif x > p.info:
                p = p.rchild #move to right child
            else:  #x found
                return True
            return False

    def min1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p.info

    def max1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info

    def min2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._min(self.root).info

    def _min(self, p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)

    def max2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._max(self.root).info

    def _max(self,p):
        if p.rchild is None:
            return p

    def insert1(self,x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                print(x,"already present in a tree")
                return
        temp = Node(x)

        if par == Node:
            self.root = temp
        elif x < par.info:
            par.lchild = temp
        else:
            par.rchild = temp
