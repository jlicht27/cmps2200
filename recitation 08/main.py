import math, time

class BinaryHeap:
    def __init__(self):
        self.H = []

    def __repr__(self):
        return str(self.H)

    # return the left child of node i
    def lchild(self, i):
        """
        See test_lchild below.

        Params:
        i....index of node
        Returns:
        j....index of the left child of node i, or -1 if n/a
        """
        if (2*i + 1) < len(self.H):
            return 2 * i + 1
        else:
            return -1

    # return the right child of node i
    def rchild(self, i):
        """
        See test_rchild below.

        Params:
        i....index of node
        Returns:
        j....index of the right child of node i, or -1 if n/a
        """
        if (2*i + 2) < len(self.H):
            return 2 * i + 2
        else:
            return -1

    # return the parent of node i
    def parent(self, i):
        """
        See test_parent below.

        Params:
        i....index of node
        Returns:
        j....index of the parent of node i, or -1 if n/a
        """
        if i > 0:
            return math.floor((i - 1) / 2)
        else:
            return -1

    def reheapUp(self, i):
        """
        Restore the heap property going upward from node i.
        Swap node i with its parent while the heap property is violated.
        See test_reheapUp.

        Params:
        i......index of the node to start with

        Returns:
        Nothing - this modifies the heap object directly.
        """
        c = i
        p = self.parent(i)
        print("reheaping up from %d"%i)
        while ((c != 0) and (self.H[c] < self.H[p])):
            #swap them
            self.H[c], self.H[p] = self.H[p], self.H[c]

            #set new child and parents
            c = self.parent(c)
            p = self.parent(c)


    # restore the heap property going downward from node i
    def reheapDown(self, i):
        """
        Restore the heap property going downward from node i.
        Swap node i with its *smaller* child while the heap property is violated.
        See test_reheapDown.

        Params:
        i......index of the node to start with

        Returns:
        Nothing - this modifies the heap object directly.
        """
        c = i
        l = self.lchild(i)
        r = self.rchild(i)
        while (((self.H[c] > self.H[l]) or (self.H[c] > self.H[r])) and (l > 0)):

            smaller = self.H.index(min(self.H[l], self.H[r]))

            self.H[c], self.H[smaller] = self.H[smaller], self.H[c]

            c = smaller
            l = self.lchild(c)
            r = self.rchild(c)


    def deleteMin(self):
        """
        Remove the root node to return its value.
        Set the last element in the heap to be the root,
        then restore the heap property using reheapDown.
        See test_deleteMin.

        Returns:
        the minimum value in the heap.
        """
        m = self.H[0]
        if (len(self.H) > 1):

            self.H[0], self.H[-1] = self.H[-1], self.H[0] #switch first and last elements
            self.H.pop(-1) #remove last element which used to be first element
            self.reheapDown(0)

        else:
            self.H.pop() # removes the only element left
        return m

    def insert(self, x):
        """
        Insert a new value x. To do so, append x
        to the list, then call reheapUp.
        See test_insert.

        Returns nothing.
        """
        self.H.append(x)

        self.reheapUp(len(self.H) - 1)

def test_lchild():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    assert heap.lchild(1) == 3
    assert heap.lchild(2) == 5
    assert heap.lchild(3) == -1

def test_rchild():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    assert heap.rchild(1) == 4
    assert heap.rchild(2) == -1

def test_parent():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    assert heap.parent(1) == 0
    assert heap.parent(2) == 0
    assert heap.parent(4) == 1
    assert heap.parent(0) == -1

def test_reheapUp():
    heap = BinaryHeap()
    # we added the 7 at the end of the list, but it is
    # out of place. We must promote it to the root.
    heap.H = [10, 12, 15, 25, 30, 36, 7]
    heap.reheapUp(6)
    assert heap.H == [7, 12, 10, 25, 30, 36, 15]

def test_reheapDown():
    heap = BinaryHeap()
    heap.H = [13, 10, 12, 15, 25, 30, 36]
    # the 13 is out of place. We must demote it one level to the left.
    heap.reheapDown(0)
    assert heap.H == [10, 13, 12, 15, 25, 30, 36]

def test_deleteMin():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    heap.deleteMin()
    print(heap.H)
    assert heap.H == [12, 25, 15, 36, 30]

def test_insert():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    heap.insert(11)
    assert heap.H == [10, 12, 11, 25, 30, 36, 15]


def heapsort(a):
    """
    Sort a list a by first creating a heap, then
    iteratively removing the smallest element to
    construct the sorted list

    Params:
    a......an unsorted list

    Returns:
    sorted version of a
    """
    H = BinaryHeap()
    sorted_a = []
    for i in a:
        H.insert(i)

    for j in a:
        sorted_a.append(H.deleteMin())

    return sorted_a

def test_heapsort():
    L = [12,5,1,6,9,10,8,2]
    assert heapsort(L) == sorted(L)
