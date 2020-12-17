import math
class Heap:
    a = []
    n = 0
    heap = []
    def __init__(self,a,n):
        self.n = n
        self.a = a
        self.heap = []
    def insert(self,k):#insert element k into the existing heap; maintain heap property
        self.heap.append(k)
        c = len(self.heap) - 1
        p = math.ceil(c/2) - 1
        while(p>=0 and c>0 and self.heap[p]>self.heap[c]):#bubble-up
            self.heap[p],self.heap[c] = self.heap[c],self.heap[p]
            c = p
            p = math.ceil(c/2) - 1
    def heapify(self):
        for i in range(self.n):
            self.insert(self.a[i])
        self.displayHeap()
    def extractMin(self):
        self.deleteAtIndex(0)
    def deleteAtIndex(self,k):#delete element at index k of the heap
        self.heap[k],self.heap[-1]=self.heap[-1],self.heap[k]
        item = self.heap.pop()
        print(item)
        lenHeap = len(self.heap)
        p = k
        lc = (2*p) + 1
        rc = (2*p) + 2
        while((lc<lenHeap and self.heap[p]>self.heap[lc]) or (rc<lenHeap and self.heap[p]>self.heap[rc])):#bubble-down
            if self.heap[lc]<self.heap[rc]:
                self.heap[lc],self.heap[p] = self.heap[p],self.heap[lc]
                p = lc
            else:
                self.heap[rc],self.heap[p] = self.heap[p],self.heap[rc]
                p = rc
            lc = (2*p) + 1
            rc = (2*p) + 2
        self.displayHeap()
    def deleteElement(self,k):#delete element k from the heap
        self.heap.remove(k)
        self.a = self.heap
        self.heap = []
        self.heapify()
        self.displayHeap()
    def displayHeap(self):
        print(self.heap)
